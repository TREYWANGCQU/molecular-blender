# -*- coding: utf-8 -*-
#
#  Molecular Blender
#  Filename: orbitals.py
#  Copyright (C) 2017 Shane Parker, Joshua Szekely
#
#  This file is part of Molecular Blender.
#
#  Molecular Blender is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3, or (at your option)
#  any later version.
#
#  Molecular Blender is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Library General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with Molecular Blender; see COPYING.
#  If not, see <http://www.gnu.org/licenses/>.
#

"""Classes and functions to compute orbital values in real space."""

import numpy as np
import math
#from .constants import ang2bohr

ang2bohr = 1.8897259885789  # pylint: disable=invalid-name

def gamma2n(i):
    """Returns Gamma(n/2), only for half-integers"""
    return np.array([gamma2n_impl(int(round(x))) for x in i])


def gamma2n_impl(i):
    """Returns gamma2n_impl(n) where n is input as 2*n=i"""
    if i <= 0:
        raise Exception("gamma2n_impl function cannot accept negative numbers")
    elif i == 2:
        return 1
    elif i == 1:
        return np.sqrt(np.pi)
    else:
        return (0.5 * i - 1.) * gamma2n_impl(i - 2)



# Polynomial functions
def polynomial_s(X, Y, Z):  # pylint: disable=unused-argument
    """n/a"""
    return np.array([1.0])

def polynomial_p(X, Y, Z):
    """x, y, z"""
    return np.array([X, Y, Z])

def polynomial_d(X, Y, Z):
    """xx, yy, zz, xy, xz, yz"""
    return np.array([X*X, Y*Y, Z*Z, X*Y*np.sqrt(3), X*Z*np.sqrt(3), Y*Z*np.sqrt(3)])

def polynomial_f(X, Y, Z):
    """xxx, yyy, zzz, xyy, xxy, xxz, xzz, yzz, yyz, xyz"""
    return np.array([X*X*X, Y*Y*Y, Z*Z*Z, X*Y*Y*np.sqrt(5), X*X*Y*np.sqrt(5), X*X*Z*np.sqrt(5),
                        X*Z*Z*np.sqrt(5), Y*Z*Z*np.sqrt(5), Y*Y*Z*np.sqrt(5), X*Y*Z*np.sqrt(15)])

def polynomial_g(X, Y, Z):
    """xxxx yyyy zzzz xxxy xxxz yyyx yyyz zzzx zzzy xxyy xxzz yyzz xxyz yyxz zzxy"""
    return np.array([X*X*X*X, Y*Y*Y*Y, Z*Z*Z*Z,
            X*X*X*Y*np.sqrt(35/5), X*X*X*Z*np.sqrt(35/5), Y*Y*Y*X*np.sqrt(35/5), Y*Y*Y*Z*np.sqrt(35/5),
            Z*Z*Z*X*np.sqrt(35/5), Z*Z*Z*Y*np.sqrt(35/5), X*X*Y*Y*np.sqrt(35/3), X*X*Z*Z*np.sqrt(35/3), Y*Y*Z*Z*np.sqrt(35/3),
            X*X*Y*Z*np.sqrt(35), Y*Y*X*Z*np.sqrt(35), Z*Z*X*Y*np.sqrt(35)])

# Plane polynomial functions
def plane_polynomial_s(XX, YY, Z):  # pylint: disable=unused-argument
    """n/a"""
    return np.ones( [ 1 ] + list(XX.shape) )

def plane_polynomial_p(XX, YY, Z):
    """x, y, z"""
    ZZ = np.full_like(XX, Z)
    return np.array([XX, YY, ZZ])

def plane_polynomial_d(XX, YY, Z):
    """xx, yy, zz, xy, xz, yz"""
    ZZ = np.full_like(XX, Z)
    return np.array([XX*XX, YY*YY, ZZ*ZZ, XX*YY*np.sqrt(3), XX*ZZ*np.sqrt(3), YY*ZZ*np.sqrt(3)])

def plane_polynomial_f(XX, YY, Z):
    """xxx, yyy, zzz, xyy, xxy, xxz, xzz, yzz, yyz, xyz"""
    ZZ = np.full_like(XX, Z)
    return np.array([XX*XX*XX, YY*YY*YY, ZZ*ZZ*ZZ, XX*YY*YY*np.sqrt(5), XX*XX*YY*np.sqrt(5), XX*XX*ZZ*np.sqrt(5),
                        XX*ZZ*ZZ*np.sqrt(5),YY*ZZ*ZZ*np.sqrt(5), YY*YY*ZZ*np.sqrt(5), XX*YY*ZZ*np.sqrt(15)])

def plane_polynomial_g(XX, YY, Z):
    """xxxx yyyy zzzz xxxy xxxz yyyx yyyz zzzx zzzy xxyy xxzz yyzz xxyz yyxz zzxy"""
    ZZ = np.full_like(XX, Z)
    return np.array([XX*XX*XX*XX, YY*YY*YY*YY, ZZ*ZZ*ZZ*ZZ,
            XX*XX*XX*YY*np.sqrt(35/5), XX*XX*XX*ZZ*np.sqrt(35/5), YY*YY*YY*XX*np.sqrt(35/5), YY*YY*YY*ZZ*np.sqrt(35/5),
            ZZ*ZZ*ZZ*XX*np.sqrt(35/5), ZZ*ZZ*ZZ*YY*np.sqrt(35/5), XX*XX*YY*YY*np.sqrt(35/3), XX*XX*ZZ*ZZ*np.sqrt(35/3), YY*YY*ZZ*ZZ*np.sqrt(35/3),
            XX*XX*YY*ZZ*np.sqrt(35), YY*YY*XX*ZZ*np.sqrt(35), ZZ*ZZ*XX*YY*np.sqrt(35)])

class Shell(object):
    """Container for shell data"""

    def __init__(self, center, l, exponents, coeff, start=0, thr=1e-6, mxx=1.0):
        self.center = np.array(center)
        self.X, self.Y, self.Z = center[0], center[1], center[2]
        self.l = int(l)
        self.exponents = np.array(exponents)
        self.coeff = np.array(coeff)

        self.start = start
        self.size = (self.l + 1) * (self.l + 2) // 2

        self.norms = 1.0 / np.sqrt(self.__norms())
        self.shellnorms = 1.0 / np.sqrt(self.__shellnorms())
        self.denormedcoeffs = self.coeff * self.shellnorms
        self.polynomial = [polynomial_s, polynomial_p,
                           polynomial_d, polynomial_f, polynomial_g][l]
        self.plane_polynomial = [plane_polynomial_s, plane_polynomial_p,
                           plane_polynomial_d, plane_polynomial_f, plane_polynomial_g][l]

        # most diffuse exponent in shell
        imin = np.argmin(self.exponents)
        self.mxx = mxx  # save max x just for use later
        self.diffuse = np.min(self.exponents)
        self.logthr = np.log(thr * mxx**self.l)
        self.mxnorm = np.max(self.norms[:, imin]) * abs(self.coeff[imin])

        self.logthr -= np.log(self.mxnorm)
        self.logthr /= -self.diffuse

    shorder = [[""],
               ["x", "y", "z"],
               ["xx", "yy", "zz", "xy", "xz", "yz"],
               ["xxx", "yyy", "zzz", "xyy", "xxy",
                "xxz", "xzz", "yzz", "yyz", "xyz"],
               ["xxxx", "yyyy", "zzzz", "xxxy", "xxxz", "yyyx", "yyyz", "zzzx", "zzzy",
                "xxyy", "xxzz", "yyzz", "xxyz", "yyxz", "zzxy"]
              ]

    def __norms(self):
        """Returns [nL, nexp] array of norms"""
        out = np.zeros([self.size, len(self.exponents)])
        for ixyz, xyz in enumerate(self.shorder[self.l]):
            cxyz = [xyz.count("x"), xyz.count("y"), xyz.count("z")]
            for ig, ex in enumerate(self.exponents):
                out[ixyz, ig] = gaussian_overlap(
                    self.center, ex, cxyz, self.center, ex, cxyz)

        return out

    def __shellnorms(self):
        """
        Returns [nexp] array of shell norms, i.e., norms of Gaussians with all angular
        in the x-direction. For example, for L=2, norms of exp(-zeta r^2) x x.
        """
        out = np.zeros_like(self.exponents)
        for ig, ex in enumerate(self.exponents):
            out[ig] = gaussian_overlap(self.center, ex, [ self.l, 0, 0 ], self.center, ex, [ self.l, 0, 0 ])
        return out

    def bounding_box_size(self, thr, logmxcoeff=0.0):
        """Returns half the edgelength of a box outside of which the shell
        is guaranteed to be below the given threshold"""
        xx = self.l * (np.log(self.mxx) - np.log(thr / self.mxnorm) + logmxcoeff) / self.diffuse
        if xx < 0:
            return 0.0
        return np.sqrt(xx)

    def value(self, x, y, z, logmxcoeff=0.0):
        """compute values of shell at point, screening out contributions below shell threshold"""
        px = x - self.X
        py = y - self.Y
        pz = z - self.Z
        rr = px * px + py * py + pz * pz

        if rr < self.logthr - logmxcoeff:
            radial = np.dot(np.exp(-1.0 * rr * self.exponents), self.denormedcoeffs)
            return radial * self.polynomial(px, py, pz)

        return None

    def plane_values(self, xx, yy, z_a, logmxcoeff=0.0):
        """compute values of shell on a plane of provided x and y values (each as an array)"""
        pxx = xx - self.X
        pyy = yy - self.Y
        pz  = z_a - self.Z

        out = np.zeros( (xx.shape[0], xx.shape[1], len(self.coeff)) )

        rr = pxx*pxx + pyy*pyy + pz * pz
        if np.any(rr < self.logthr - logmxcoeff):
            expz = np.exp(np.einsum("xy,e->xye", -1.0*rr, self.exponents))
            radial = np.einsum("xye,e->xy", expz, self.denormedcoeffs)
            out = self.plane_polynomial(pxx, pyy, pz)
            for p in range(out.shape[0]):
                out[p,:,:] *= radial
            return out
        else:
            return None

def gaussian_overlap(axyz, aexp, apoly, bxyz, bexp, bpoly):
    """returns overlap integral for gaussians centered at xyz with exponents exp
    and angular momentum poly"""
    assert (axyz == bxyz).all()  # too lazy to do two-center overlap for now
    abpoly = [k + n for k, n in zip(apoly, bpoly)]
    if any([i % 2 == 1 for i in abpoly]):
        return 0.0
    abpoly = np.array(abpoly) + 1.
    fac = np.power(aexp + bexp, -0.5 * abpoly)
    gam = gamma2n(abpoly)
    return np.prod(fac * gam)


class MOData(object):
    """Organizes data for computing orbitals in real space"""

    def __init__(self, shells, coeff, nocc):
        assert sum([sh.size for sh in shells]) == coeff.shape[1]

        self.shells = shells
        self.coeff = coeff
        self.nocc = nocc

    def homo(self):
        return self.nocc

    def get_orbital(self, iorb):
        """Returns OrbitalCalculater for orbital"""
        i = (iorb if iorb > 0 else self.nocc + iorb) - 1
        return OrbitalCalculater(self.shells, self.coeff[i, :])

    @classmethod
    def from_dict(cls, geo):
        """Builds MOData out of the dict object available in MolecularBlender"""
        shells = []
        ico = 0
        for atom, ash in zip(geo["atoms"], geo["basis"]):
            # make sure centers are given in bohr
            xyz = [x * ang2bohr for x in atom["position"]]
            for sh in ash:
                newshell = Shell(xyz, "spdfg".index(
                    sh["shell"]), sh["exponents"], sh["contractions"], start=ico)
                ico += newshell.size
                shells.append(newshell)

        nocc = sum([float(x["occup"]) > 0.0 for x in geo["mo"]])
        nmo = len(geo["mo"])
        nao = sum([sh.size for sh in shells])

        coeff = np.zeros([nmo, nao])
        for i in range(nmo):
            coeff[i, :] = geo["mo"][i]["coeff"]

        return cls(shells, coeff, nocc)


class OrbitalCalculater(object):
    """Computes value of orbital at real space points"""

    def __init__(self, shells, coeff):
        self.shells = shells
        self.coeff = coeff

        # use very small number to replace zeros
        self.logmxcoeff = np.log(np.array([
            max(np.max(abs(self.coeff[sh.start:sh.start + sh.size])), 1e-30)
            for sh in self.shells]))

    def bounding_box(self, thr=1.0e-5):
        """returns lower and upper limits of box (in bohr) that should fully contain orbital"""
        # find lower bounds
        p0 = [np.min([sh.center[ixyz] - sh.bounding_box_size(thr, lmx)
                      for sh, lmx in zip(self.shells, self.logmxcoeff)]) for ixyz in range(3)]

        # find upper bounds
        p1 = [np.max([sh.center[ixyz] + sh.bounding_box_size(thr, lmx)
                      for sh, lmx in zip(self.shells, self.logmxcoeff)]) for ixyz in range(3)]

        return p0, p1

    def value(self, x, y, z):
        """Returns value of the orbital at specified point"""
        out = 0.0
        for sh, lmx in zip(self.shells, self.logmxcoeff):
            val = sh.value(x, y, z, logmxcoeff=lmx)
            if val is not None:
                out += np.dot(val, self.coeff[sh.start:sh.start + sh.size])
        return out

    def plane_values(self, xvals, yvals, z_a):
        xx = np.zeros([len(xvals), len(yvals)])
        yy = np.zeros([len(xvals), len(yvals)])
        for i, x in enumerate(xvals):
            xx[i,:] = x
            yy[i,:] = yvals[:]

        out = np.zeros([len(xvals), len(yvals)])
        for sh, lmx in zip(self.shells, self.logmxcoeff):
            vals = sh.plane_values(xx, yy, z_a, logmxcoeff=lmx)
            if vals is not None:
                out += np.einsum("pxy,p->xy", vals, self.coeff[sh.start:sh.start+sh.size])
        return out

    def box_values(self, xvals, yvals, zvals):
        out = np.zeros([len(xvals), len(yvals), len(zvals)])

        for k, z_a in enumerate(zvals):
            out[:,:,k] = self.plane_values(xvals, yvals, z_a)

        return out

    def isovalue_containing_proportion(self, values=[0.90], resolution=0.2*ang2bohr, box=None):
        if box is None:
            p0, p1 = self.bounding_box(1e-4)

        npoints = [ int(math.ceil((b - a)/resolution)) for a, b in zip(p0, p1) ]

        xvals, yvals, zvals = [ np.linspace(a, b, num=n, endpoint=True ) for a, b, n in zip(p0, p1, npoints) ]
        dV = (xvals[1] - xvals[0]) * (yvals[1] - yvals[0]) * (zvals[1] - zvals[0])
        boxvalues = self.box_values(xvals, yvals, zvals).reshape(-1)

        return [0.1]
        return isovalue_containing_proportion(values, boxvalues, dV)
