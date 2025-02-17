#    Copyright (C) 2020 David J. Wooten
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

import numpy as np


def jacobian(
    d1, d2, E0, E1, E2, E3, logh1, logh2, logC1, logC2, r1r, r2r, logalpha12, logalpha21, loggamma12, loggamma21
):
    """Evaluates Jacobian of MuSyC (gamma)

    Returns:
    -----------
    jacobian : tuple
        j_E0, j_E1, j_E2, j_E3, j_logh1, j_logh2, j_logC1, j_logC2, j_logalpha12, j_logalpha21, j_loggamma12,
        j_loggamma21
    """
    h1 = np.exp(logh1)
    h2 = np.exp(logh2)
    C1 = np.exp(logC1)
    C2 = np.exp(logC2)
    alpha12 = np.exp(logalpha12)
    alpha21 = np.exp(logalpha21)
    gamma12 = np.exp(loggamma12)
    gamma21 = np.exp(loggamma21)

    logd1 = np.log(d1)
    logd2 = np.log(d2)

    logd1alpha21 = np.log(d1 * alpha21)
    logd2alpha12 = np.log(d2 * alpha12)

    d1_pow_h1 = np.float_power(d1, h1)
    d2_pow_h2 = np.float_power(d2, h2)

    C1_pow_h1 = np.float_power(C1, h1)
    C2_pow_h2 = np.float_power(C2, h2)

    r1 = r1r / C1_pow_h1
    r2 = r2r / C2_pow_h2

    alpha21d1_pow_gamma21h1 = np.float_power(alpha21 * d1, gamma21 * h1)
    alpha12d2_pow_gamma12h2 = np.float_power(alpha12 * d2, gamma12 * h2)

    r1_pow_gamma21p1 = np.float_power(r1, gamma21 + 1)
    r2_pow_gamma12p1 = np.float_power(r2, gamma12 + 1)
    r2C2h2_pow_gamma12 = np.float_power(r2 * C2_pow_h2, gamma12)
    r1C1h1_pow_gamma21 = np.float_power(r1 * C1_pow_h1, gamma21)

    r2_pow_gamma12 = np.float_power(r2, gamma12)
    r1_pow_gamma21 = np.float_power(r1, gamma21)
    log = np.log

    # ********** logh1 ********

    j_logh1 = (
        E0
        * (
            r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * C2_pow_h2
            + r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * C2_pow_h2
            + r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * C1_pow_h1
            + r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * C2_pow_h2
        )
        * (
            -d1_pow_h1 * r1 * r2 * r1C1h1_pow_gamma21 * C2_pow_h2 * gamma21 * h1 * logC1
            - d1_pow_h1 * r1 * r2 * r1C1h1_pow_gamma21 * C2_pow_h2 * h1 * logd1
            - d1_pow_h1 * r1 * r2 * r2C2h2_pow_gamma12 * C2_pow_h2 * h1 * logd1
            - d1_pow_h1 * r1 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * C2_pow_h2 * h1 * logd1
            - d1_pow_h1 * r1 * r2_pow_gamma12 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * gamma21 * h1 * logC1
            - d1_pow_h1 * r1 * r2_pow_gamma12 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * h1 * logd1
            - d1_pow_h1
            * r1_pow_gamma21p1
            * r2_pow_gamma12
            * alpha21d1_pow_gamma21h1
            * alpha12d2_pow_gamma12h2
            * h1
            * logd1
            - d1_pow_h1
            * r1_pow_gamma21p1
            * r2_pow_gamma12
            * alpha21d1_pow_gamma21h1
            * alpha12d2_pow_gamma12h2
            * (gamma21 * h1)
            * logd1alpha21
            - d1_pow_h1 * r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * h1 * logd1
            - d1_pow_h1
            * r1_pow_gamma21p1
            * alpha21d1_pow_gamma21h1
            * r2C2h2_pow_gamma12
            * (gamma21 * h1)
            * logd1alpha21
            - d2_pow_h2 * r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * gamma21 * h1 * logC1
            - d2_pow_h2 * r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * h1 * logC1
            - d2_pow_h2 * r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * h1 * logC1
            - d2_pow_h2 * r1_pow_gamma21p1 * r2 * alpha21d1_pow_gamma21h1 * C1_pow_h1 * h1 * logC1
            - d2_pow_h2 * r1_pow_gamma21p1 * r2 * alpha21d1_pow_gamma21h1 * C1_pow_h1 * (gamma21 * h1) * logd1alpha21
            - d2_pow_h2
            * r1_pow_gamma21
            * r2
            * alpha21d1_pow_gamma21h1
            * r2C2h2_pow_gamma12
            * (gamma21 * h1)
            * logd1alpha21
            - d2_pow_h2
            * r1_pow_gamma21
            * r2_pow_gamma12p1
            * alpha21d1_pow_gamma21h1
            * alpha12d2_pow_gamma12h2
            * (gamma21 * h1)
            * logd1alpha21
            - d2_pow_h2 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * gamma21 * h1 * logC1
            - r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * C2_pow_h2 * gamma21 * h1 * logC1
            - r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * C2_pow_h2 * h1 * logC1
            - r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * C2_pow_h2 * h1 * logC1
            - r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * C1_pow_h1 * h1 * logC1
            - r1_pow_gamma21p1
            * alpha21d1_pow_gamma21h1
            * r2C2h2_pow_gamma12
            * C1_pow_h1
            * (gamma21 * h1)
            * logd1alpha21
            - r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * C2_pow_h2 * gamma21 * h1 * logC1
        )
        / (
            d1_pow_h1 * r1 * r2 * r1C1h1_pow_gamma21 * C2_pow_h2
            + d1_pow_h1 * r1 * r2 * r2C2h2_pow_gamma12 * C2_pow_h2
            + d1_pow_h1 * r1 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * C2_pow_h2
            + d1_pow_h1 * r1 * r2_pow_gamma12 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + d1_pow_h1 * r1_pow_gamma21p1 * r2_pow_gamma12 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
            + d1_pow_h1 * r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1
            + d2_pow_h2 * r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1
            + d2_pow_h2 * r1_pow_gamma21p1 * r2 * alpha21d1_pow_gamma21h1 * C1_pow_h1
            + d2_pow_h2 * r1_pow_gamma21 * r2 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1_pow_gamma21 * r2_pow_gamma12p1 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
            + d2_pow_h2 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * C2_pow_h2
            + r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * C2_pow_h2
            + r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * C1_pow_h1
            + r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * C2_pow_h2
        )
        ** 2
        + E0
        * (
            r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * C2_pow_h2 * gamma21 * h1 * logC1
            + r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * C2_pow_h2 * h1 * logC1
            + r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * C2_pow_h2 * h1 * logC1
            + r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * C1_pow_h1 * h1 * logC1
            + r1_pow_gamma21p1
            * alpha21d1_pow_gamma21h1
            * r2C2h2_pow_gamma12
            * C1_pow_h1
            * (gamma21 * h1)
            * logd1alpha21
            + r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * C2_pow_h2 * gamma21 * h1 * logC1
        )
        / (
            d1_pow_h1 * r1 * r2 * r1C1h1_pow_gamma21 * C2_pow_h2
            + d1_pow_h1 * r1 * r2 * r2C2h2_pow_gamma12 * C2_pow_h2
            + d1_pow_h1 * r1 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * C2_pow_h2
            + d1_pow_h1 * r1 * r2_pow_gamma12 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + d1_pow_h1 * r1_pow_gamma21p1 * r2_pow_gamma12 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
            + d1_pow_h1 * r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1
            + d2_pow_h2 * r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1
            + d2_pow_h2 * r1_pow_gamma21p1 * r2 * alpha21d1_pow_gamma21h1 * C1_pow_h1
            + d2_pow_h2 * r1_pow_gamma21 * r2 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1_pow_gamma21 * r2_pow_gamma12p1 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
            + d2_pow_h2 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * C2_pow_h2
            + r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * C2_pow_h2
            + r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * C1_pow_h1
            + r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * C2_pow_h2
        )
        + E1
        * (
            d1_pow_h1 * r1 * r2 * r1C1h1_pow_gamma21 * C2_pow_h2
            + d1_pow_h1 * r1 * r2 * r2C2h2_pow_gamma12 * C2_pow_h2
            + d1_pow_h1 * r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1_pow_gamma21 * r2 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
        )
        * (
            -d1_pow_h1 * r1 * r2 * r1C1h1_pow_gamma21 * C2_pow_h2 * gamma21 * h1 * logC1
            - d1_pow_h1 * r1 * r2 * r1C1h1_pow_gamma21 * C2_pow_h2 * h1 * logd1
            - d1_pow_h1 * r1 * r2 * r2C2h2_pow_gamma12 * C2_pow_h2 * h1 * logd1
            - d1_pow_h1 * r1 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * C2_pow_h2 * h1 * logd1
            - d1_pow_h1 * r1 * r2_pow_gamma12 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * gamma21 * h1 * logC1
            - d1_pow_h1 * r1 * r2_pow_gamma12 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * h1 * logd1
            - d1_pow_h1
            * r1_pow_gamma21p1
            * r2_pow_gamma12
            * alpha21d1_pow_gamma21h1
            * alpha12d2_pow_gamma12h2
            * h1
            * logd1
            - d1_pow_h1
            * r1_pow_gamma21p1
            * r2_pow_gamma12
            * alpha21d1_pow_gamma21h1
            * alpha12d2_pow_gamma12h2
            * (gamma21 * h1)
            * logd1alpha21
            - d1_pow_h1 * r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * h1 * logd1
            - d1_pow_h1
            * r1_pow_gamma21p1
            * alpha21d1_pow_gamma21h1
            * r2C2h2_pow_gamma12
            * (gamma21 * h1)
            * logd1alpha21
            - d2_pow_h2 * r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * gamma21 * h1 * logC1
            - d2_pow_h2 * r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * h1 * logC1
            - d2_pow_h2 * r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * h1 * logC1
            - d2_pow_h2 * r1_pow_gamma21p1 * r2 * alpha21d1_pow_gamma21h1 * C1_pow_h1 * h1 * logC1
            - d2_pow_h2 * r1_pow_gamma21p1 * r2 * alpha21d1_pow_gamma21h1 * C1_pow_h1 * (gamma21 * h1) * logd1alpha21
            - d2_pow_h2
            * r1_pow_gamma21
            * r2
            * alpha21d1_pow_gamma21h1
            * r2C2h2_pow_gamma12
            * (gamma21 * h1)
            * logd1alpha21
            - d2_pow_h2
            * r1_pow_gamma21
            * r2_pow_gamma12p1
            * alpha21d1_pow_gamma21h1
            * alpha12d2_pow_gamma12h2
            * (gamma21 * h1)
            * logd1alpha21
            - d2_pow_h2 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * gamma21 * h1 * logC1
            - r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * C2_pow_h2 * gamma21 * h1 * logC1
            - r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * C2_pow_h2 * h1 * logC1
            - r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * C2_pow_h2 * h1 * logC1
            - r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * C1_pow_h1 * h1 * logC1
            - r1_pow_gamma21p1
            * alpha21d1_pow_gamma21h1
            * r2C2h2_pow_gamma12
            * C1_pow_h1
            * (gamma21 * h1)
            * logd1alpha21
            - r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * C2_pow_h2 * gamma21 * h1 * logC1
        )
        / (
            d1_pow_h1 * r1 * r2 * r1C1h1_pow_gamma21 * C2_pow_h2
            + d1_pow_h1 * r1 * r2 * r2C2h2_pow_gamma12 * C2_pow_h2
            + d1_pow_h1 * r1 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * C2_pow_h2
            + d1_pow_h1 * r1 * r2_pow_gamma12 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + d1_pow_h1 * r1_pow_gamma21p1 * r2_pow_gamma12 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
            + d1_pow_h1 * r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1
            + d2_pow_h2 * r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1
            + d2_pow_h2 * r1_pow_gamma21p1 * r2 * alpha21d1_pow_gamma21h1 * C1_pow_h1
            + d2_pow_h2 * r1_pow_gamma21 * r2 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1_pow_gamma21 * r2_pow_gamma12p1 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
            + d2_pow_h2 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * C2_pow_h2
            + r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * C2_pow_h2
            + r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * C1_pow_h1
            + r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * C2_pow_h2
        )
        ** 2
        + E1
        * (
            d1_pow_h1 * r1 * r2 * r1C1h1_pow_gamma21 * C2_pow_h2 * gamma21 * h1 * logC1
            + d1_pow_h1 * r1 * r2 * r1C1h1_pow_gamma21 * C2_pow_h2 * h1 * logd1
            + d1_pow_h1 * r1 * r2 * r2C2h2_pow_gamma12 * C2_pow_h2 * h1 * logd1
            + d1_pow_h1 * r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * h1 * logd1
            + d1_pow_h1
            * r1_pow_gamma21p1
            * alpha21d1_pow_gamma21h1
            * r2C2h2_pow_gamma12
            * (gamma21 * h1)
            * logd1alpha21
            + d2_pow_h2
            * r1_pow_gamma21
            * r2
            * alpha21d1_pow_gamma21h1
            * r2C2h2_pow_gamma12
            * (gamma21 * h1)
            * logd1alpha21
        )
        / (
            d1_pow_h1 * r1 * r2 * r1C1h1_pow_gamma21 * C2_pow_h2
            + d1_pow_h1 * r1 * r2 * r2C2h2_pow_gamma12 * C2_pow_h2
            + d1_pow_h1 * r1 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * C2_pow_h2
            + d1_pow_h1 * r1 * r2_pow_gamma12 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + d1_pow_h1 * r1_pow_gamma21p1 * r2_pow_gamma12 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
            + d1_pow_h1 * r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1
            + d2_pow_h2 * r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1
            + d2_pow_h2 * r1_pow_gamma21p1 * r2 * alpha21d1_pow_gamma21h1 * C1_pow_h1
            + d2_pow_h2 * r1_pow_gamma21 * r2 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1_pow_gamma21 * r2_pow_gamma12p1 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
            + d2_pow_h2 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * C2_pow_h2
            + r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * C2_pow_h2
            + r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * C1_pow_h1
            + r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * C2_pow_h2
        )
        + E2
        * (
            d1_pow_h1 * r1 * r2_pow_gamma12 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + d2_pow_h2 * r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1
            + d2_pow_h2 * r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1
            + d2_pow_h2 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
        )
        * (
            -d1_pow_h1 * r1 * r2 * r1C1h1_pow_gamma21 * C2_pow_h2 * gamma21 * h1 * logC1
            - d1_pow_h1 * r1 * r2 * r1C1h1_pow_gamma21 * C2_pow_h2 * h1 * logd1
            - d1_pow_h1 * r1 * r2 * r2C2h2_pow_gamma12 * C2_pow_h2 * h1 * logd1
            - d1_pow_h1 * r1 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * C2_pow_h2 * h1 * logd1
            - d1_pow_h1 * r1 * r2_pow_gamma12 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * gamma21 * h1 * logC1
            - d1_pow_h1 * r1 * r2_pow_gamma12 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * h1 * logd1
            - d1_pow_h1
            * r1_pow_gamma21p1
            * r2_pow_gamma12
            * alpha21d1_pow_gamma21h1
            * alpha12d2_pow_gamma12h2
            * h1
            * logd1
            - d1_pow_h1
            * r1_pow_gamma21p1
            * r2_pow_gamma12
            * alpha21d1_pow_gamma21h1
            * alpha12d2_pow_gamma12h2
            * (gamma21 * h1)
            * logd1alpha21
            - d1_pow_h1 * r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * h1 * logd1
            - d1_pow_h1
            * r1_pow_gamma21p1
            * alpha21d1_pow_gamma21h1
            * r2C2h2_pow_gamma12
            * (gamma21 * h1)
            * logd1alpha21
            - d2_pow_h2 * r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * gamma21 * h1 * logC1
            - d2_pow_h2 * r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * h1 * logC1
            - d2_pow_h2 * r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * h1 * logC1
            - d2_pow_h2 * r1_pow_gamma21p1 * r2 * alpha21d1_pow_gamma21h1 * C1_pow_h1 * h1 * logC1
            - d2_pow_h2 * r1_pow_gamma21p1 * r2 * alpha21d1_pow_gamma21h1 * C1_pow_h1 * (gamma21 * h1) * logd1alpha21
            - d2_pow_h2
            * r1_pow_gamma21
            * r2
            * alpha21d1_pow_gamma21h1
            * r2C2h2_pow_gamma12
            * (gamma21 * h1)
            * logd1alpha21
            - d2_pow_h2
            * r1_pow_gamma21
            * r2_pow_gamma12p1
            * alpha21d1_pow_gamma21h1
            * alpha12d2_pow_gamma12h2
            * (gamma21 * h1)
            * logd1alpha21
            - d2_pow_h2 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * gamma21 * h1 * logC1
            - r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * C2_pow_h2 * gamma21 * h1 * logC1
            - r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * C2_pow_h2 * h1 * logC1
            - r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * C2_pow_h2 * h1 * logC1
            - r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * C1_pow_h1 * h1 * logC1
            - r1_pow_gamma21p1
            * alpha21d1_pow_gamma21h1
            * r2C2h2_pow_gamma12
            * C1_pow_h1
            * (gamma21 * h1)
            * logd1alpha21
            - r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * C2_pow_h2 * gamma21 * h1 * logC1
        )
        / (
            d1_pow_h1 * r1 * r2 * r1C1h1_pow_gamma21 * C2_pow_h2
            + d1_pow_h1 * r1 * r2 * r2C2h2_pow_gamma12 * C2_pow_h2
            + d1_pow_h1 * r1 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * C2_pow_h2
            + d1_pow_h1 * r1 * r2_pow_gamma12 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + d1_pow_h1 * r1_pow_gamma21p1 * r2_pow_gamma12 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
            + d1_pow_h1 * r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1
            + d2_pow_h2 * r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1
            + d2_pow_h2 * r1_pow_gamma21p1 * r2 * alpha21d1_pow_gamma21h1 * C1_pow_h1
            + d2_pow_h2 * r1_pow_gamma21 * r2 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1_pow_gamma21 * r2_pow_gamma12p1 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
            + d2_pow_h2 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * C2_pow_h2
            + r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * C2_pow_h2
            + r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * C1_pow_h1
            + r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * C2_pow_h2
        )
        ** 2
        + E2
        * (
            d1_pow_h1 * r1 * r2_pow_gamma12 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * gamma21 * h1 * logC1
            + d1_pow_h1 * r1 * r2_pow_gamma12 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * h1 * logd1
            + d2_pow_h2 * r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * gamma21 * h1 * logC1
            + d2_pow_h2 * r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * h1 * logC1
            + d2_pow_h2 * r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * h1 * logC1
            + d2_pow_h2 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * gamma21 * h1 * logC1
        )
        / (
            d1_pow_h1 * r1 * r2 * r1C1h1_pow_gamma21 * C2_pow_h2
            + d1_pow_h1 * r1 * r2 * r2C2h2_pow_gamma12 * C2_pow_h2
            + d1_pow_h1 * r1 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * C2_pow_h2
            + d1_pow_h1 * r1 * r2_pow_gamma12 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + d1_pow_h1 * r1_pow_gamma21p1 * r2_pow_gamma12 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
            + d1_pow_h1 * r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1
            + d2_pow_h2 * r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1
            + d2_pow_h2 * r1_pow_gamma21p1 * r2 * alpha21d1_pow_gamma21h1 * C1_pow_h1
            + d2_pow_h2 * r1_pow_gamma21 * r2 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1_pow_gamma21 * r2_pow_gamma12p1 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
            + d2_pow_h2 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * C2_pow_h2
            + r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * C2_pow_h2
            + r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * C1_pow_h1
            + r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * C2_pow_h2
        )
        + E3
        * (
            d2_pow_h2
            * r1
            * r2
            * (
                d1_pow_h1 * r1 * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r1 * C1_pow_h1)
                - (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r2 * C2_pow_h2)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
            * C1_pow_h1
            * h1
            * logC1
            + d2_pow_h2
            * r2
            * (r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            * (
                d1_pow_h1 * r1 * (d1_pow_h1 * r1 * h1 * logd1 + r1 * C1_pow_h1 * h1 * logC1)
                + d1_pow_h1
                * r1
                * (-d1_pow_h1 * r1 - r1 * C1_pow_h1 - r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
                * h1
                * logd1
                + d1_pow_h1 * r1 * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r1 * C1_pow_h1) * h1 * logd1
                + (-d1_pow_h1 * r1 * h1 * logd1 - r1 * C1_pow_h1 * h1 * logC1)
                * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r2 * C2_pow_h2)
            )
            + (
                d1_pow_h1 * r1 * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r1 * C1_pow_h1)
                - (d1_pow_h1 * r1 + d2_pow_h2 * r2)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
            * (
                d1_pow_h1 * d2_pow_h2 * r1 * r2 * h1 * logd1
                + r1_pow_gamma21
                * alpha21d1_pow_gamma21h1
                * (-d1_pow_h1 * r1 - r1 * C1_pow_h1 - r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
                * (gamma21 * h1)
                * logd1alpha21
                + (-d1_pow_h1 * r1 * h1 * logd1 - r1 * C1_pow_h1 * h1 * logC1)
                * (d2_pow_h2 * r2 + r1_pow_gamma21 * alpha21d1_pow_gamma21h1 + r2 * C2_pow_h2)
            )
            + (
                d1_pow_h1 * d2_pow_h2 * r1 * r2
                - (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
                * (d2_pow_h2 * r2 + r1_pow_gamma21 * alpha21d1_pow_gamma21h1 + r2 * C2_pow_h2)
            )
            * (
                d1_pow_h1 * r1 * (d1_pow_h1 * r1 * h1 * logd1 + r1 * C1_pow_h1 * h1 * logC1)
                + d1_pow_h1 * r1 * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r1 * C1_pow_h1) * h1 * logd1
                - d1_pow_h1
                * r1
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
                * h1
                * logd1
                + (-d1_pow_h1 * r1 - d2_pow_h2 * r2) * (d1_pow_h1 * r1 * h1 * logd1 + r1 * C1_pow_h1 * h1 * logC1)
            )
        )
        / (
            -(
                (-d1_pow_h1 * r1 + r2C2h2_pow_gamma12) * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r1 * C1_pow_h1)
                + (d1_pow_h1 * r1 + d2_pow_h2 * r2)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
            * (
                d1_pow_h1 * d2_pow_h2 * r1 * r2
                - (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
                * (d2_pow_h2 * r2 + r1_pow_gamma21 * alpha21d1_pow_gamma21h1 + r2 * C2_pow_h2)
            )
            + (
                d1_pow_h1 * r1 * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r1 * C1_pow_h1)
                - (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r2 * C2_pow_h2)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
            * (
                -d2_pow_h2 * r2 * (d1_pow_h1 * r1 - r2C2h2_pow_gamma12)
                + (d2_pow_h2 * r2 - r1C1h1_pow_gamma21)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
        )
        + E3
        * (
            d2_pow_h2
            * r2
            * (r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            * (
                d1_pow_h1 * r1 * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r1 * C1_pow_h1)
                - (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r2 * C2_pow_h2)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
            + (
                d1_pow_h1 * r1 * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r1 * C1_pow_h1)
                - (d1_pow_h1 * r1 + d2_pow_h2 * r2)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
            * (
                d1_pow_h1 * d2_pow_h2 * r1 * r2
                - (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
                * (d2_pow_h2 * r2 + r1_pow_gamma21 * alpha21d1_pow_gamma21h1 + r2 * C2_pow_h2)
            )
        )
        * (
            -(
                -(-d1_pow_h1 * r1 + r2C2h2_pow_gamma12) * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r1 * C1_pow_h1)
                - (d1_pow_h1 * r1 + d2_pow_h2 * r2)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
            * (
                d1_pow_h1 * d2_pow_h2 * r1 * r2 * h1 * logd1
                + r1_pow_gamma21
                * alpha21d1_pow_gamma21h1
                * (-d1_pow_h1 * r1 - r1 * C1_pow_h1 - r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
                * (gamma21 * h1)
                * logd1alpha21
                + (-d1_pow_h1 * r1 * h1 * logd1 - r1 * C1_pow_h1 * h1 * logC1)
                * (d2_pow_h2 * r2 + r1_pow_gamma21 * alpha21d1_pow_gamma21h1 + r2 * C2_pow_h2)
            )
            - (
                d1_pow_h1 * r1 * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r1 * C1_pow_h1)
                - (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r2 * C2_pow_h2)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
            * (
                -d1_pow_h1 * d2_pow_h2 * r1 * r2 * h1 * logd1
                - r1C1h1_pow_gamma21
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
                * gamma21
                * h1
                * logC1
                + (d2_pow_h2 * r2 - r1C1h1_pow_gamma21) * (d1_pow_h1 * r1 * h1 * logd1 + r1 * C1_pow_h1 * h1 * logC1)
            )
            - (
                -d2_pow_h2 * r2 * (d1_pow_h1 * r1 - r2C2h2_pow_gamma12)
                + (d2_pow_h2 * r2 - r1C1h1_pow_gamma21)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
            * (
                d1_pow_h1 * r1 * (d1_pow_h1 * r1 * h1 * logd1 + r1 * C1_pow_h1 * h1 * logC1)
                + d1_pow_h1
                * r1
                * (-d1_pow_h1 * r1 - r1 * C1_pow_h1 - r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
                * h1
                * logd1
                + d1_pow_h1 * r1 * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r1 * C1_pow_h1) * h1 * logd1
                + (-d1_pow_h1 * r1 * h1 * logd1 - r1 * C1_pow_h1 * h1 * logC1)
                * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r2 * C2_pow_h2)
            )
            - (
                d1_pow_h1 * d2_pow_h2 * r1 * r2
                - (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
                * (d2_pow_h2 * r2 + r1_pow_gamma21 * alpha21d1_pow_gamma21h1 + r2 * C2_pow_h2)
            )
            * (
                d1_pow_h1 * r1 * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r1 * C1_pow_h1) * h1 * logd1
                - d1_pow_h1
                * r1
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
                * h1
                * logd1
                - (-d1_pow_h1 * r1 + r2C2h2_pow_gamma12) * (d1_pow_h1 * r1 * h1 * logd1 + r1 * C1_pow_h1 * h1 * logC1)
                - (d1_pow_h1 * r1 + d2_pow_h2 * r2) * (d1_pow_h1 * r1 * h1 * logd1 + r1 * C1_pow_h1 * h1 * logC1)
            )
        )
        / (
            -(
                (-d1_pow_h1 * r1 + r2C2h2_pow_gamma12) * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r1 * C1_pow_h1)
                + (d1_pow_h1 * r1 + d2_pow_h2 * r2)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
            * (
                d1_pow_h1 * d2_pow_h2 * r1 * r2
                - (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
                * (d2_pow_h2 * r2 + r1_pow_gamma21 * alpha21d1_pow_gamma21h1 + r2 * C2_pow_h2)
            )
            + (
                d1_pow_h1 * r1 * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r1 * C1_pow_h1)
                - (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r2 * C2_pow_h2)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
            * (
                -d2_pow_h2 * r2 * (d1_pow_h1 * r1 - r2C2h2_pow_gamma12)
                + (d2_pow_h2 * r2 - r1C1h1_pow_gamma21)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
        )
        ** 2
    )

    # ********** logh2 ********

    j_logh2 = (
        E0
        * (
            r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * C2_pow_h2
            + r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * C2_pow_h2
            + r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * C1_pow_h1
            + r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * C2_pow_h2
        )
        * (
            -d1_pow_h1 * r1 * r2 * r1C1h1_pow_gamma21 * C2_pow_h2 * h2 * logC2
            - d1_pow_h1 * r1 * r2 * r2C2h2_pow_gamma12 * C2_pow_h2 * gamma12 * h2 * logC2
            - d1_pow_h1 * r1 * r2 * r2C2h2_pow_gamma12 * C2_pow_h2 * h2 * logC2
            - d1_pow_h1 * r1 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * C2_pow_h2 * h2 * logC2
            - d1_pow_h1 * r1 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * C2_pow_h2 * (gamma12 * h2) * logd2alpha12
            - d1_pow_h1
            * r1
            * r2_pow_gamma12
            * alpha12d2_pow_gamma12h2
            * r1C1h1_pow_gamma21
            * (gamma12 * h2)
            * logd2alpha12
            - d1_pow_h1
            * r1_pow_gamma21p1
            * r2_pow_gamma12
            * alpha21d1_pow_gamma21h1
            * alpha12d2_pow_gamma12h2
            * (gamma12 * h2)
            * logd2alpha12
            - d1_pow_h1 * r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * gamma12 * h2 * logC2
            - d2_pow_h2 * r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * h2 * logd2
            - d2_pow_h2 * r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * gamma12 * h2 * logC2
            - d2_pow_h2 * r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * h2 * logd2
            - d2_pow_h2 * r1_pow_gamma21p1 * r2 * alpha21d1_pow_gamma21h1 * C1_pow_h1 * h2 * logd2
            - d2_pow_h2 * r1_pow_gamma21 * r2 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * gamma12 * h2 * logC2
            - d2_pow_h2 * r1_pow_gamma21 * r2 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * h2 * logd2
            - d2_pow_h2
            * r1_pow_gamma21
            * r2_pow_gamma12p1
            * alpha21d1_pow_gamma21h1
            * alpha12d2_pow_gamma12h2
            * h2
            * logd2
            - d2_pow_h2
            * r1_pow_gamma21
            * r2_pow_gamma12p1
            * alpha21d1_pow_gamma21h1
            * alpha12d2_pow_gamma12h2
            * (gamma12 * h2)
            * logd2alpha12
            - d2_pow_h2 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * h2 * logd2
            - d2_pow_h2
            * r2_pow_gamma12p1
            * alpha12d2_pow_gamma12h2
            * r1C1h1_pow_gamma21
            * (gamma12 * h2)
            * logd2alpha12
            - r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * C2_pow_h2 * h2 * logC2
            - r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * C2_pow_h2 * gamma12 * h2 * logC2
            - r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * C2_pow_h2 * h2 * logC2
            - r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * C1_pow_h1 * gamma12 * h2 * logC2
            - r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * C2_pow_h2 * h2 * logC2
            - r2_pow_gamma12p1
            * alpha12d2_pow_gamma12h2
            * r1C1h1_pow_gamma21
            * C2_pow_h2
            * (gamma12 * h2)
            * logd2alpha12
        )
        / (
            d1_pow_h1 * r1 * r2 * r1C1h1_pow_gamma21 * C2_pow_h2
            + d1_pow_h1 * r1 * r2 * r2C2h2_pow_gamma12 * C2_pow_h2
            + d1_pow_h1 * r1 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * C2_pow_h2
            + d1_pow_h1 * r1 * r2_pow_gamma12 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + d1_pow_h1 * r1_pow_gamma21p1 * r2_pow_gamma12 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
            + d1_pow_h1 * r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1
            + d2_pow_h2 * r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1
            + d2_pow_h2 * r1_pow_gamma21p1 * r2 * alpha21d1_pow_gamma21h1 * C1_pow_h1
            + d2_pow_h2 * r1_pow_gamma21 * r2 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1_pow_gamma21 * r2_pow_gamma12p1 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
            + d2_pow_h2 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * C2_pow_h2
            + r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * C2_pow_h2
            + r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * C1_pow_h1
            + r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * C2_pow_h2
        )
        ** 2
        + E0
        * (
            r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * C2_pow_h2 * h2 * logC2
            + r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * C2_pow_h2 * gamma12 * h2 * logC2
            + r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * C2_pow_h2 * h2 * logC2
            + r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * C1_pow_h1 * gamma12 * h2 * logC2
            + r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * C2_pow_h2 * h2 * logC2
            + r2_pow_gamma12p1
            * alpha12d2_pow_gamma12h2
            * r1C1h1_pow_gamma21
            * C2_pow_h2
            * (gamma12 * h2)
            * logd2alpha12
        )
        / (
            d1_pow_h1 * r1 * r2 * r1C1h1_pow_gamma21 * C2_pow_h2
            + d1_pow_h1 * r1 * r2 * r2C2h2_pow_gamma12 * C2_pow_h2
            + d1_pow_h1 * r1 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * C2_pow_h2
            + d1_pow_h1 * r1 * r2_pow_gamma12 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + d1_pow_h1 * r1_pow_gamma21p1 * r2_pow_gamma12 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
            + d1_pow_h1 * r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1
            + d2_pow_h2 * r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1
            + d2_pow_h2 * r1_pow_gamma21p1 * r2 * alpha21d1_pow_gamma21h1 * C1_pow_h1
            + d2_pow_h2 * r1_pow_gamma21 * r2 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1_pow_gamma21 * r2_pow_gamma12p1 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
            + d2_pow_h2 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * C2_pow_h2
            + r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * C2_pow_h2
            + r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * C1_pow_h1
            + r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * C2_pow_h2
        )
        + E1
        * (
            d1_pow_h1 * r1 * r2 * r1C1h1_pow_gamma21 * C2_pow_h2
            + d1_pow_h1 * r1 * r2 * r2C2h2_pow_gamma12 * C2_pow_h2
            + d1_pow_h1 * r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1_pow_gamma21 * r2 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
        )
        * (
            -d1_pow_h1 * r1 * r2 * r1C1h1_pow_gamma21 * C2_pow_h2 * h2 * logC2
            - d1_pow_h1 * r1 * r2 * r2C2h2_pow_gamma12 * C2_pow_h2 * gamma12 * h2 * logC2
            - d1_pow_h1 * r1 * r2 * r2C2h2_pow_gamma12 * C2_pow_h2 * h2 * logC2
            - d1_pow_h1 * r1 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * C2_pow_h2 * h2 * logC2
            - d1_pow_h1 * r1 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * C2_pow_h2 * (gamma12 * h2) * logd2alpha12
            - d1_pow_h1
            * r1
            * r2_pow_gamma12
            * alpha12d2_pow_gamma12h2
            * r1C1h1_pow_gamma21
            * (gamma12 * h2)
            * logd2alpha12
            - d1_pow_h1
            * r1_pow_gamma21p1
            * r2_pow_gamma12
            * alpha21d1_pow_gamma21h1
            * alpha12d2_pow_gamma12h2
            * (gamma12 * h2)
            * logd2alpha12
            - d1_pow_h1 * r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * gamma12 * h2 * logC2
            - d2_pow_h2 * r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * h2 * logd2
            - d2_pow_h2 * r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * gamma12 * h2 * logC2
            - d2_pow_h2 * r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * h2 * logd2
            - d2_pow_h2 * r1_pow_gamma21p1 * r2 * alpha21d1_pow_gamma21h1 * C1_pow_h1 * h2 * logd2
            - d2_pow_h2 * r1_pow_gamma21 * r2 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * gamma12 * h2 * logC2
            - d2_pow_h2 * r1_pow_gamma21 * r2 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * h2 * logd2
            - d2_pow_h2
            * r1_pow_gamma21
            * r2_pow_gamma12p1
            * alpha21d1_pow_gamma21h1
            * alpha12d2_pow_gamma12h2
            * h2
            * logd2
            - d2_pow_h2
            * r1_pow_gamma21
            * r2_pow_gamma12p1
            * alpha21d1_pow_gamma21h1
            * alpha12d2_pow_gamma12h2
            * (gamma12 * h2)
            * logd2alpha12
            - d2_pow_h2 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * h2 * logd2
            - d2_pow_h2
            * r2_pow_gamma12p1
            * alpha12d2_pow_gamma12h2
            * r1C1h1_pow_gamma21
            * (gamma12 * h2)
            * logd2alpha12
            - r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * C2_pow_h2 * h2 * logC2
            - r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * C2_pow_h2 * gamma12 * h2 * logC2
            - r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * C2_pow_h2 * h2 * logC2
            - r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * C1_pow_h1 * gamma12 * h2 * logC2
            - r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * C2_pow_h2 * h2 * logC2
            - r2_pow_gamma12p1
            * alpha12d2_pow_gamma12h2
            * r1C1h1_pow_gamma21
            * C2_pow_h2
            * (gamma12 * h2)
            * logd2alpha12
        )
        / (
            d1_pow_h1 * r1 * r2 * r1C1h1_pow_gamma21 * C2_pow_h2
            + d1_pow_h1 * r1 * r2 * r2C2h2_pow_gamma12 * C2_pow_h2
            + d1_pow_h1 * r1 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * C2_pow_h2
            + d1_pow_h1 * r1 * r2_pow_gamma12 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + d1_pow_h1 * r1_pow_gamma21p1 * r2_pow_gamma12 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
            + d1_pow_h1 * r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1
            + d2_pow_h2 * r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1
            + d2_pow_h2 * r1_pow_gamma21p1 * r2 * alpha21d1_pow_gamma21h1 * C1_pow_h1
            + d2_pow_h2 * r1_pow_gamma21 * r2 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1_pow_gamma21 * r2_pow_gamma12p1 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
            + d2_pow_h2 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * C2_pow_h2
            + r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * C2_pow_h2
            + r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * C1_pow_h1
            + r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * C2_pow_h2
        )
        ** 2
        + E1
        * (
            d1_pow_h1 * r1 * r2 * r1C1h1_pow_gamma21 * C2_pow_h2 * h2 * logC2
            + d1_pow_h1 * r1 * r2 * r2C2h2_pow_gamma12 * C2_pow_h2 * gamma12 * h2 * logC2
            + d1_pow_h1 * r1 * r2 * r2C2h2_pow_gamma12 * C2_pow_h2 * h2 * logC2
            + d1_pow_h1 * r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * gamma12 * h2 * logC2
            + d2_pow_h2 * r1_pow_gamma21 * r2 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * gamma12 * h2 * logC2
            + d2_pow_h2 * r1_pow_gamma21 * r2 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * h2 * logd2
        )
        / (
            d1_pow_h1 * r1 * r2 * r1C1h1_pow_gamma21 * C2_pow_h2
            + d1_pow_h1 * r1 * r2 * r2C2h2_pow_gamma12 * C2_pow_h2
            + d1_pow_h1 * r1 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * C2_pow_h2
            + d1_pow_h1 * r1 * r2_pow_gamma12 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + d1_pow_h1 * r1_pow_gamma21p1 * r2_pow_gamma12 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
            + d1_pow_h1 * r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1
            + d2_pow_h2 * r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1
            + d2_pow_h2 * r1_pow_gamma21p1 * r2 * alpha21d1_pow_gamma21h1 * C1_pow_h1
            + d2_pow_h2 * r1_pow_gamma21 * r2 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1_pow_gamma21 * r2_pow_gamma12p1 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
            + d2_pow_h2 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * C2_pow_h2
            + r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * C2_pow_h2
            + r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * C1_pow_h1
            + r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * C2_pow_h2
        )
        + E2
        * (
            d1_pow_h1 * r1 * r2_pow_gamma12 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + d2_pow_h2 * r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1
            + d2_pow_h2 * r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1
            + d2_pow_h2 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
        )
        * (
            -d1_pow_h1 * r1 * r2 * r1C1h1_pow_gamma21 * C2_pow_h2 * h2 * logC2
            - d1_pow_h1 * r1 * r2 * r2C2h2_pow_gamma12 * C2_pow_h2 * gamma12 * h2 * logC2
            - d1_pow_h1 * r1 * r2 * r2C2h2_pow_gamma12 * C2_pow_h2 * h2 * logC2
            - d1_pow_h1 * r1 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * C2_pow_h2 * h2 * logC2
            - d1_pow_h1 * r1 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * C2_pow_h2 * (gamma12 * h2) * logd2alpha12
            - d1_pow_h1
            * r1
            * r2_pow_gamma12
            * alpha12d2_pow_gamma12h2
            * r1C1h1_pow_gamma21
            * (gamma12 * h2)
            * logd2alpha12
            - d1_pow_h1
            * r1_pow_gamma21p1
            * r2_pow_gamma12
            * alpha21d1_pow_gamma21h1
            * alpha12d2_pow_gamma12h2
            * (gamma12 * h2)
            * logd2alpha12
            - d1_pow_h1 * r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * gamma12 * h2 * logC2
            - d2_pow_h2 * r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * h2 * logd2
            - d2_pow_h2 * r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * gamma12 * h2 * logC2
            - d2_pow_h2 * r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * h2 * logd2
            - d2_pow_h2 * r1_pow_gamma21p1 * r2 * alpha21d1_pow_gamma21h1 * C1_pow_h1 * h2 * logd2
            - d2_pow_h2 * r1_pow_gamma21 * r2 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * gamma12 * h2 * logC2
            - d2_pow_h2 * r1_pow_gamma21 * r2 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * h2 * logd2
            - d2_pow_h2
            * r1_pow_gamma21
            * r2_pow_gamma12p1
            * alpha21d1_pow_gamma21h1
            * alpha12d2_pow_gamma12h2
            * h2
            * logd2
            - d2_pow_h2
            * r1_pow_gamma21
            * r2_pow_gamma12p1
            * alpha21d1_pow_gamma21h1
            * alpha12d2_pow_gamma12h2
            * (gamma12 * h2)
            * logd2alpha12
            - d2_pow_h2 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * h2 * logd2
            - d2_pow_h2
            * r2_pow_gamma12p1
            * alpha12d2_pow_gamma12h2
            * r1C1h1_pow_gamma21
            * (gamma12 * h2)
            * logd2alpha12
            - r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * C2_pow_h2 * h2 * logC2
            - r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * C2_pow_h2 * gamma12 * h2 * logC2
            - r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * C2_pow_h2 * h2 * logC2
            - r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * C1_pow_h1 * gamma12 * h2 * logC2
            - r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * C2_pow_h2 * h2 * logC2
            - r2_pow_gamma12p1
            * alpha12d2_pow_gamma12h2
            * r1C1h1_pow_gamma21
            * C2_pow_h2
            * (gamma12 * h2)
            * logd2alpha12
        )
        / (
            d1_pow_h1 * r1 * r2 * r1C1h1_pow_gamma21 * C2_pow_h2
            + d1_pow_h1 * r1 * r2 * r2C2h2_pow_gamma12 * C2_pow_h2
            + d1_pow_h1 * r1 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * C2_pow_h2
            + d1_pow_h1 * r1 * r2_pow_gamma12 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + d1_pow_h1 * r1_pow_gamma21p1 * r2_pow_gamma12 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
            + d1_pow_h1 * r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1
            + d2_pow_h2 * r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1
            + d2_pow_h2 * r1_pow_gamma21p1 * r2 * alpha21d1_pow_gamma21h1 * C1_pow_h1
            + d2_pow_h2 * r1_pow_gamma21 * r2 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1_pow_gamma21 * r2_pow_gamma12p1 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
            + d2_pow_h2 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * C2_pow_h2
            + r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * C2_pow_h2
            + r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * C1_pow_h1
            + r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * C2_pow_h2
        )
        ** 2
        + E2
        * (
            d1_pow_h1
            * r1
            * r2_pow_gamma12
            * alpha12d2_pow_gamma12h2
            * r1C1h1_pow_gamma21
            * (gamma12 * h2)
            * logd2alpha12
            + d2_pow_h2 * r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * h2 * logd2
            + d2_pow_h2 * r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * gamma12 * h2 * logC2
            + d2_pow_h2 * r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * h2 * logd2
            + d2_pow_h2 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * h2 * logd2
            + d2_pow_h2
            * r2_pow_gamma12p1
            * alpha12d2_pow_gamma12h2
            * r1C1h1_pow_gamma21
            * (gamma12 * h2)
            * logd2alpha12
        )
        / (
            d1_pow_h1 * r1 * r2 * r1C1h1_pow_gamma21 * C2_pow_h2
            + d1_pow_h1 * r1 * r2 * r2C2h2_pow_gamma12 * C2_pow_h2
            + d1_pow_h1 * r1 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * C2_pow_h2
            + d1_pow_h1 * r1 * r2_pow_gamma12 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + d1_pow_h1 * r1_pow_gamma21p1 * r2_pow_gamma12 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
            + d1_pow_h1 * r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1
            + d2_pow_h2 * r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1
            + d2_pow_h2 * r1_pow_gamma21p1 * r2 * alpha21d1_pow_gamma21h1 * C1_pow_h1
            + d2_pow_h2 * r1_pow_gamma21 * r2 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1_pow_gamma21 * r2_pow_gamma12p1 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
            + d2_pow_h2 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * C2_pow_h2
            + r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * C2_pow_h2
            + r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * C1_pow_h1
            + r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * C2_pow_h2
        )
        + E3
        * (
            d2_pow_h2
            * r2
            * r2_pow_gamma12
            * alpha12d2_pow_gamma12h2
            * (
                d1_pow_h1 * r1 * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r1 * C1_pow_h1)
                - (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r2 * C2_pow_h2)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
            * (gamma12 * h2)
            * logd2alpha12
            + d2_pow_h2
            * r2
            * (r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            * (
                d1_pow_h1 * r1 * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r1 * C1_pow_h1)
                - (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r2 * C2_pow_h2)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
            * h2
            * logd2
            + d2_pow_h2
            * r2
            * (r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            * (
                d1_pow_h1 * d2_pow_h2 * r1 * r2 * h2 * logd2
                - r2_pow_gamma12
                * alpha12d2_pow_gamma12h2
                * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r2 * C2_pow_h2)
                * (gamma12 * h2)
                * logd2alpha12
                + (d2_pow_h2 * r2 * h2 * logd2 + r2 * C2_pow_h2 * h2 * logC2)
                * (-d1_pow_h1 * r1 - r1 * C1_pow_h1 - r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
            + (
                d1_pow_h1 * r1 * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r1 * C1_pow_h1)
                - (d1_pow_h1 * r1 + d2_pow_h2 * r2)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
            * (
                d1_pow_h1 * d2_pow_h2 * r1 * r2 * h2 * logd2
                - r2_pow_gamma12
                * alpha12d2_pow_gamma12h2
                * (d2_pow_h2 * r2 + r1_pow_gamma21 * alpha21d1_pow_gamma21h1 + r2 * C2_pow_h2)
                * (gamma12 * h2)
                * logd2alpha12
                + (d2_pow_h2 * r2 * h2 * logd2 + r2 * C2_pow_h2 * h2 * logC2)
                * (-d1_pow_h1 * r1 - r1 * C1_pow_h1 - r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
            + (
                d1_pow_h1 * d2_pow_h2 * r1 * r2
                - (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
                * (d2_pow_h2 * r2 + r1_pow_gamma21 * alpha21d1_pow_gamma21h1 + r2 * C2_pow_h2)
            )
            * (
                d1_pow_h1 * d2_pow_h2 * r1 * r2 * h2 * logd2
                - d2_pow_h2
                * r2
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
                * h2
                * logd2
                + r2_pow_gamma12
                * alpha12d2_pow_gamma12h2
                * (-d1_pow_h1 * r1 - d2_pow_h2 * r2)
                * (gamma12 * h2)
                * logd2alpha12
            )
        )
        / (
            -(
                (-d1_pow_h1 * r1 + r2C2h2_pow_gamma12) * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r1 * C1_pow_h1)
                + (d1_pow_h1 * r1 + d2_pow_h2 * r2)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
            * (
                d1_pow_h1 * d2_pow_h2 * r1 * r2
                - (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
                * (d2_pow_h2 * r2 + r1_pow_gamma21 * alpha21d1_pow_gamma21h1 + r2 * C2_pow_h2)
            )
            + (
                d1_pow_h1 * r1 * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r1 * C1_pow_h1)
                - (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r2 * C2_pow_h2)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
            * (
                -d2_pow_h2 * r2 * (d1_pow_h1 * r1 - r2C2h2_pow_gamma12)
                + (d2_pow_h2 * r2 - r1C1h1_pow_gamma21)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
        )
        + E3
        * (
            d2_pow_h2
            * r2
            * (r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            * (
                d1_pow_h1 * r1 * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r1 * C1_pow_h1)
                - (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r2 * C2_pow_h2)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
            + (
                d1_pow_h1 * r1 * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r1 * C1_pow_h1)
                - (d1_pow_h1 * r1 + d2_pow_h2 * r2)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
            * (
                d1_pow_h1 * d2_pow_h2 * r1 * r2
                - (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
                * (d2_pow_h2 * r2 + r1_pow_gamma21 * alpha21d1_pow_gamma21h1 + r2 * C2_pow_h2)
            )
        )
        * (
            -(
                -(-d1_pow_h1 * r1 + r2C2h2_pow_gamma12) * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r1 * C1_pow_h1)
                - (d1_pow_h1 * r1 + d2_pow_h2 * r2)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
            * (
                d1_pow_h1 * d2_pow_h2 * r1 * r2 * h2 * logd2
                - r2_pow_gamma12
                * alpha12d2_pow_gamma12h2
                * (d2_pow_h2 * r2 + r1_pow_gamma21 * alpha21d1_pow_gamma21h1 + r2 * C2_pow_h2)
                * (gamma12 * h2)
                * logd2alpha12
                + (d2_pow_h2 * r2 * h2 * logd2 + r2 * C2_pow_h2 * h2 * logC2)
                * (-d1_pow_h1 * r1 - r1 * C1_pow_h1 - r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
            - (
                d1_pow_h1 * r1 * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r1 * C1_pow_h1)
                - (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r2 * C2_pow_h2)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
            * (
                d2_pow_h2 * r2 * r2C2h2_pow_gamma12 * gamma12 * h2 * logC2
                - d2_pow_h2 * r2 * (d1_pow_h1 * r1 - r2C2h2_pow_gamma12) * h2 * logd2
                + d2_pow_h2
                * r2
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
                * h2
                * logd2
                + r2_pow_gamma12
                * alpha12d2_pow_gamma12h2
                * (d2_pow_h2 * r2 - r1C1h1_pow_gamma21)
                * (gamma12 * h2)
                * logd2alpha12
            )
            - (
                -d2_pow_h2 * r2 * (d1_pow_h1 * r1 - r2C2h2_pow_gamma12)
                + (d2_pow_h2 * r2 - r1C1h1_pow_gamma21)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
            * (
                d1_pow_h1 * d2_pow_h2 * r1 * r2 * h2 * logd2
                - r2_pow_gamma12
                * alpha12d2_pow_gamma12h2
                * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r2 * C2_pow_h2)
                * (gamma12 * h2)
                * logd2alpha12
                + (d2_pow_h2 * r2 * h2 * logd2 + r2 * C2_pow_h2 * h2 * logC2)
                * (-d1_pow_h1 * r1 - r1 * C1_pow_h1 - r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
            - (
                d1_pow_h1 * d2_pow_h2 * r1 * r2
                - (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
                * (d2_pow_h2 * r2 + r1_pow_gamma21 * alpha21d1_pow_gamma21h1 + r2 * C2_pow_h2)
            )
            * (
                -d2_pow_h2 * r2 * (-d1_pow_h1 * r1 + r2C2h2_pow_gamma12) * h2 * logd2
                - d2_pow_h2
                * r2
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
                * h2
                * logd2
                - r2_pow_gamma12
                * alpha12d2_pow_gamma12h2
                * (d1_pow_h1 * r1 + d2_pow_h2 * r2)
                * (gamma12 * h2)
                * logd2alpha12
                - r2C2h2_pow_gamma12 * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r1 * C1_pow_h1) * gamma12 * h2 * logC2
            )
        )
        / (
            -(
                (-d1_pow_h1 * r1 + r2C2h2_pow_gamma12) * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r1 * C1_pow_h1)
                + (d1_pow_h1 * r1 + d2_pow_h2 * r2)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
            * (
                d1_pow_h1 * d2_pow_h2 * r1 * r2
                - (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
                * (d2_pow_h2 * r2 + r1_pow_gamma21 * alpha21d1_pow_gamma21h1 + r2 * C2_pow_h2)
            )
            + (
                d1_pow_h1 * r1 * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r1 * C1_pow_h1)
                - (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r2 * C2_pow_h2)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
            * (
                -d2_pow_h2 * r2 * (d1_pow_h1 * r1 - r2C2h2_pow_gamma12)
                + (d2_pow_h2 * r2 - r1C1h1_pow_gamma21)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
        )
        ** 2
    )

    # ********** logC1 ********

    j_logC1 = (
        E0
        * (
            r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * C2_pow_h2
            + r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * C2_pow_h2
            + r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * C1_pow_h1
            + r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * C2_pow_h2
        )
        * (
            -d1_pow_h1 * r1 * r2 * r1C1h1_pow_gamma21 * C2_pow_h2 * gamma21 * h1
            - d1_pow_h1 * r1 * r2_pow_gamma12 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * gamma21 * h1
            - d2_pow_h2 * r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * gamma21 * h1
            - d2_pow_h2 * r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * h1
            - d2_pow_h2 * r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * h1
            - d2_pow_h2 * r1_pow_gamma21p1 * r2 * alpha21d1_pow_gamma21h1 * C1_pow_h1 * h1
            - d2_pow_h2 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * gamma21 * h1
            - r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * C2_pow_h2 * gamma21 * h1
            - r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * C2_pow_h2 * h1
            - r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * C2_pow_h2 * h1
            - r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * C1_pow_h1 * h1
            - r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * C2_pow_h2 * gamma21 * h1
        )
        / (
            d1_pow_h1 * r1 * r2 * r1C1h1_pow_gamma21 * C2_pow_h2
            + d1_pow_h1 * r1 * r2 * r2C2h2_pow_gamma12 * C2_pow_h2
            + d1_pow_h1 * r1 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * C2_pow_h2
            + d1_pow_h1 * r1 * r2_pow_gamma12 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + d1_pow_h1 * r1_pow_gamma21p1 * r2_pow_gamma12 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
            + d1_pow_h1 * r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1
            + d2_pow_h2 * r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1
            + d2_pow_h2 * r1_pow_gamma21p1 * r2 * alpha21d1_pow_gamma21h1 * C1_pow_h1
            + d2_pow_h2 * r1_pow_gamma21 * r2 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1_pow_gamma21 * r2_pow_gamma12p1 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
            + d2_pow_h2 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * C2_pow_h2
            + r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * C2_pow_h2
            + r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * C1_pow_h1
            + r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * C2_pow_h2
        )
        ** 2
        + E0
        * (
            r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * C2_pow_h2 * gamma21 * h1
            + r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * C2_pow_h2 * h1
            + r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * C2_pow_h2 * h1
            + r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * C1_pow_h1 * h1
            + r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * C2_pow_h2 * gamma21 * h1
        )
        / (
            d1_pow_h1 * r1 * r2 * r1C1h1_pow_gamma21 * C2_pow_h2
            + d1_pow_h1 * r1 * r2 * r2C2h2_pow_gamma12 * C2_pow_h2
            + d1_pow_h1 * r1 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * C2_pow_h2
            + d1_pow_h1 * r1 * r2_pow_gamma12 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + d1_pow_h1 * r1_pow_gamma21p1 * r2_pow_gamma12 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
            + d1_pow_h1 * r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1
            + d2_pow_h2 * r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1
            + d2_pow_h2 * r1_pow_gamma21p1 * r2 * alpha21d1_pow_gamma21h1 * C1_pow_h1
            + d2_pow_h2 * r1_pow_gamma21 * r2 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1_pow_gamma21 * r2_pow_gamma12p1 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
            + d2_pow_h2 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * C2_pow_h2
            + r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * C2_pow_h2
            + r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * C1_pow_h1
            + r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * C2_pow_h2
        )
        + E1
        * d1_pow_h1
        * r1
        * r2
        * r1C1h1_pow_gamma21
        * C2_pow_h2
        * gamma21
        * h1
        / (
            d1_pow_h1 * r1 * r2 * r1C1h1_pow_gamma21 * C2_pow_h2
            + d1_pow_h1 * r1 * r2 * r2C2h2_pow_gamma12 * C2_pow_h2
            + d1_pow_h1 * r1 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * C2_pow_h2
            + d1_pow_h1 * r1 * r2_pow_gamma12 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + d1_pow_h1 * r1_pow_gamma21p1 * r2_pow_gamma12 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
            + d1_pow_h1 * r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1
            + d2_pow_h2 * r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1
            + d2_pow_h2 * r1_pow_gamma21p1 * r2 * alpha21d1_pow_gamma21h1 * C1_pow_h1
            + d2_pow_h2 * r1_pow_gamma21 * r2 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1_pow_gamma21 * r2_pow_gamma12p1 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
            + d2_pow_h2 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * C2_pow_h2
            + r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * C2_pow_h2
            + r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * C1_pow_h1
            + r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * C2_pow_h2
        )
        + E1
        * (
            d1_pow_h1 * r1 * r2 * r1C1h1_pow_gamma21 * C2_pow_h2
            + d1_pow_h1 * r1 * r2 * r2C2h2_pow_gamma12 * C2_pow_h2
            + d1_pow_h1 * r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1_pow_gamma21 * r2 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
        )
        * (
            -d1_pow_h1 * r1 * r2 * r1C1h1_pow_gamma21 * C2_pow_h2 * gamma21 * h1
            - d1_pow_h1 * r1 * r2_pow_gamma12 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * gamma21 * h1
            - d2_pow_h2 * r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * gamma21 * h1
            - d2_pow_h2 * r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * h1
            - d2_pow_h2 * r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * h1
            - d2_pow_h2 * r1_pow_gamma21p1 * r2 * alpha21d1_pow_gamma21h1 * C1_pow_h1 * h1
            - d2_pow_h2 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * gamma21 * h1
            - r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * C2_pow_h2 * gamma21 * h1
            - r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * C2_pow_h2 * h1
            - r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * C2_pow_h2 * h1
            - r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * C1_pow_h1 * h1
            - r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * C2_pow_h2 * gamma21 * h1
        )
        / (
            d1_pow_h1 * r1 * r2 * r1C1h1_pow_gamma21 * C2_pow_h2
            + d1_pow_h1 * r1 * r2 * r2C2h2_pow_gamma12 * C2_pow_h2
            + d1_pow_h1 * r1 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * C2_pow_h2
            + d1_pow_h1 * r1 * r2_pow_gamma12 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + d1_pow_h1 * r1_pow_gamma21p1 * r2_pow_gamma12 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
            + d1_pow_h1 * r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1
            + d2_pow_h2 * r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1
            + d2_pow_h2 * r1_pow_gamma21p1 * r2 * alpha21d1_pow_gamma21h1 * C1_pow_h1
            + d2_pow_h2 * r1_pow_gamma21 * r2 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1_pow_gamma21 * r2_pow_gamma12p1 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
            + d2_pow_h2 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * C2_pow_h2
            + r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * C2_pow_h2
            + r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * C1_pow_h1
            + r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * C2_pow_h2
        )
        ** 2
        + E2
        * (
            d1_pow_h1 * r1 * r2_pow_gamma12 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + d2_pow_h2 * r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1
            + d2_pow_h2 * r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1
            + d2_pow_h2 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
        )
        * (
            -d1_pow_h1 * r1 * r2 * r1C1h1_pow_gamma21 * C2_pow_h2 * gamma21 * h1
            - d1_pow_h1 * r1 * r2_pow_gamma12 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * gamma21 * h1
            - d2_pow_h2 * r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * gamma21 * h1
            - d2_pow_h2 * r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * h1
            - d2_pow_h2 * r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * h1
            - d2_pow_h2 * r1_pow_gamma21p1 * r2 * alpha21d1_pow_gamma21h1 * C1_pow_h1 * h1
            - d2_pow_h2 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * gamma21 * h1
            - r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * C2_pow_h2 * gamma21 * h1
            - r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * C2_pow_h2 * h1
            - r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * C2_pow_h2 * h1
            - r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * C1_pow_h1 * h1
            - r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * C2_pow_h2 * gamma21 * h1
        )
        / (
            d1_pow_h1 * r1 * r2 * r1C1h1_pow_gamma21 * C2_pow_h2
            + d1_pow_h1 * r1 * r2 * r2C2h2_pow_gamma12 * C2_pow_h2
            + d1_pow_h1 * r1 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * C2_pow_h2
            + d1_pow_h1 * r1 * r2_pow_gamma12 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + d1_pow_h1 * r1_pow_gamma21p1 * r2_pow_gamma12 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
            + d1_pow_h1 * r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1
            + d2_pow_h2 * r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1
            + d2_pow_h2 * r1_pow_gamma21p1 * r2 * alpha21d1_pow_gamma21h1 * C1_pow_h1
            + d2_pow_h2 * r1_pow_gamma21 * r2 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1_pow_gamma21 * r2_pow_gamma12p1 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
            + d2_pow_h2 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * C2_pow_h2
            + r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * C2_pow_h2
            + r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * C1_pow_h1
            + r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * C2_pow_h2
        )
        ** 2
        + E2
        * (
            d1_pow_h1 * r1 * r2_pow_gamma12 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * gamma21 * h1
            + d2_pow_h2 * r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * gamma21 * h1
            + d2_pow_h2 * r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * h1
            + d2_pow_h2 * r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * h1
            + d2_pow_h2 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * gamma21 * h1
        )
        / (
            d1_pow_h1 * r1 * r2 * r1C1h1_pow_gamma21 * C2_pow_h2
            + d1_pow_h1 * r1 * r2 * r2C2h2_pow_gamma12 * C2_pow_h2
            + d1_pow_h1 * r1 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * C2_pow_h2
            + d1_pow_h1 * r1 * r2_pow_gamma12 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + d1_pow_h1 * r1_pow_gamma21p1 * r2_pow_gamma12 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
            + d1_pow_h1 * r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1
            + d2_pow_h2 * r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1
            + d2_pow_h2 * r1_pow_gamma21p1 * r2 * alpha21d1_pow_gamma21h1 * C1_pow_h1
            + d2_pow_h2 * r1_pow_gamma21 * r2 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1_pow_gamma21 * r2_pow_gamma12p1 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
            + d2_pow_h2 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * C2_pow_h2
            + r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * C2_pow_h2
            + r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * C1_pow_h1
            + r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * C2_pow_h2
        )
        + E3
        * (
            d2_pow_h2
            * r1
            * r2
            * (
                d1_pow_h1 * r1 * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r1 * C1_pow_h1)
                - (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r2 * C2_pow_h2)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
            * C1_pow_h1
            * h1
            + d2_pow_h2
            * r2
            * (r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            * (
                d1_pow_h1 * r1**2 * C1_pow_h1 * h1
                - r1 * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r2 * C2_pow_h2) * C1_pow_h1 * h1
            )
            - r1
            * (
                d1_pow_h1 * r1 * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r1 * C1_pow_h1)
                - (d1_pow_h1 * r1 + d2_pow_h2 * r2)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
            * (d2_pow_h2 * r2 + r1_pow_gamma21 * alpha21d1_pow_gamma21h1 + r2 * C2_pow_h2)
            * C1_pow_h1
            * h1
            + (
                d1_pow_h1 * d2_pow_h2 * r1 * r2
                - (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
                * (d2_pow_h2 * r2 + r1_pow_gamma21 * alpha21d1_pow_gamma21h1 + r2 * C2_pow_h2)
            )
            * (d1_pow_h1 * r1**2 * C1_pow_h1 * h1 + r1 * (-d1_pow_h1 * r1 - d2_pow_h2 * r2) * C1_pow_h1 * h1)
        )
        / (
            -(
                (-d1_pow_h1 * r1 + r2C2h2_pow_gamma12) * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r1 * C1_pow_h1)
                + (d1_pow_h1 * r1 + d2_pow_h2 * r2)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
            * (
                d1_pow_h1 * d2_pow_h2 * r1 * r2
                - (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
                * (d2_pow_h2 * r2 + r1_pow_gamma21 * alpha21d1_pow_gamma21h1 + r2 * C2_pow_h2)
            )
            + (
                d1_pow_h1 * r1 * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r1 * C1_pow_h1)
                - (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r2 * C2_pow_h2)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
            * (
                -d2_pow_h2 * r2 * (d1_pow_h1 * r1 - r2C2h2_pow_gamma12)
                + (d2_pow_h2 * r2 - r1C1h1_pow_gamma21)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
        )
        + E3
        * (
            d2_pow_h2
            * r2
            * (r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            * (
                d1_pow_h1 * r1 * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r1 * C1_pow_h1)
                - (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r2 * C2_pow_h2)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
            + (
                d1_pow_h1 * r1 * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r1 * C1_pow_h1)
                - (d1_pow_h1 * r1 + d2_pow_h2 * r2)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
            * (
                d1_pow_h1 * d2_pow_h2 * r1 * r2
                - (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
                * (d2_pow_h2 * r2 + r1_pow_gamma21 * alpha21d1_pow_gamma21h1 + r2 * C2_pow_h2)
            )
        )
        * (
            r1
            * (
                -(-d1_pow_h1 * r1 + r2C2h2_pow_gamma12) * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r1 * C1_pow_h1)
                - (d1_pow_h1 * r1 + d2_pow_h2 * r2)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
            * (d2_pow_h2 * r2 + r1_pow_gamma21 * alpha21d1_pow_gamma21h1 + r2 * C2_pow_h2)
            * C1_pow_h1
            * h1
            - (
                d1_pow_h1 * r1 * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r1 * C1_pow_h1)
                - (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r2 * C2_pow_h2)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
            * (
                r1 * (d2_pow_h2 * r2 - r1C1h1_pow_gamma21) * C1_pow_h1 * h1
                - r1C1h1_pow_gamma21
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
                * gamma21
                * h1
            )
            - (
                -d2_pow_h2 * r2 * (d1_pow_h1 * r1 - r2C2h2_pow_gamma12)
                + (d2_pow_h2 * r2 - r1C1h1_pow_gamma21)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
            * (
                d1_pow_h1 * r1**2 * C1_pow_h1 * h1
                - r1 * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r2 * C2_pow_h2) * C1_pow_h1 * h1
            )
            - (
                d1_pow_h1 * d2_pow_h2 * r1 * r2
                - (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
                * (d2_pow_h2 * r2 + r1_pow_gamma21 * alpha21d1_pow_gamma21h1 + r2 * C2_pow_h2)
            )
            * (
                -r1 * (-d1_pow_h1 * r1 + r2C2h2_pow_gamma12) * C1_pow_h1 * h1
                - r1 * (d1_pow_h1 * r1 + d2_pow_h2 * r2) * C1_pow_h1 * h1
            )
        )
        / (
            -(
                (-d1_pow_h1 * r1 + r2C2h2_pow_gamma12) * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r1 * C1_pow_h1)
                + (d1_pow_h1 * r1 + d2_pow_h2 * r2)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
            * (
                d1_pow_h1 * d2_pow_h2 * r1 * r2
                - (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
                * (d2_pow_h2 * r2 + r1_pow_gamma21 * alpha21d1_pow_gamma21h1 + r2 * C2_pow_h2)
            )
            + (
                d1_pow_h1 * r1 * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r1 * C1_pow_h1)
                - (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r2 * C2_pow_h2)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
            * (
                -d2_pow_h2 * r2 * (d1_pow_h1 * r1 - r2C2h2_pow_gamma12)
                + (d2_pow_h2 * r2 - r1C1h1_pow_gamma21)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
        )
        ** 2
    )

    # ********** logC2 ********

    j_logC2 = (
        E0
        * (
            r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * C2_pow_h2
            + r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * C2_pow_h2
            + r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * C1_pow_h1
            + r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * C2_pow_h2
        )
        * (
            -d1_pow_h1 * r1 * r2 * r1C1h1_pow_gamma21 * C2_pow_h2 * h2
            - d1_pow_h1 * r1 * r2 * r2C2h2_pow_gamma12 * C2_pow_h2 * gamma12 * h2
            - d1_pow_h1 * r1 * r2 * r2C2h2_pow_gamma12 * C2_pow_h2 * h2
            - d1_pow_h1 * r1 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * C2_pow_h2 * h2
            - d1_pow_h1 * r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * gamma12 * h2
            - d2_pow_h2 * r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * gamma12 * h2
            - d2_pow_h2 * r1_pow_gamma21 * r2 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * gamma12 * h2
            - r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * C2_pow_h2 * h2
            - r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * C2_pow_h2 * gamma12 * h2
            - r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * C2_pow_h2 * h2
            - r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * C1_pow_h1 * gamma12 * h2
            - r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * C2_pow_h2 * h2
        )
        / (
            d1_pow_h1 * r1 * r2 * r1C1h1_pow_gamma21 * C2_pow_h2
            + d1_pow_h1 * r1 * r2 * r2C2h2_pow_gamma12 * C2_pow_h2
            + d1_pow_h1 * r1 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * C2_pow_h2
            + d1_pow_h1 * r1 * r2_pow_gamma12 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + d1_pow_h1 * r1_pow_gamma21p1 * r2_pow_gamma12 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
            + d1_pow_h1 * r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1
            + d2_pow_h2 * r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1
            + d2_pow_h2 * r1_pow_gamma21p1 * r2 * alpha21d1_pow_gamma21h1 * C1_pow_h1
            + d2_pow_h2 * r1_pow_gamma21 * r2 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1_pow_gamma21 * r2_pow_gamma12p1 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
            + d2_pow_h2 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * C2_pow_h2
            + r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * C2_pow_h2
            + r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * C1_pow_h1
            + r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * C2_pow_h2
        )
        ** 2
        + E0
        * (
            r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * C2_pow_h2 * h2
            + r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * C2_pow_h2 * gamma12 * h2
            + r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * C2_pow_h2 * h2
            + r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * C1_pow_h1 * gamma12 * h2
            + r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * C2_pow_h2 * h2
        )
        / (
            d1_pow_h1 * r1 * r2 * r1C1h1_pow_gamma21 * C2_pow_h2
            + d1_pow_h1 * r1 * r2 * r2C2h2_pow_gamma12 * C2_pow_h2
            + d1_pow_h1 * r1 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * C2_pow_h2
            + d1_pow_h1 * r1 * r2_pow_gamma12 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + d1_pow_h1 * r1_pow_gamma21p1 * r2_pow_gamma12 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
            + d1_pow_h1 * r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1
            + d2_pow_h2 * r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1
            + d2_pow_h2 * r1_pow_gamma21p1 * r2 * alpha21d1_pow_gamma21h1 * C1_pow_h1
            + d2_pow_h2 * r1_pow_gamma21 * r2 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1_pow_gamma21 * r2_pow_gamma12p1 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
            + d2_pow_h2 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * C2_pow_h2
            + r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * C2_pow_h2
            + r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * C1_pow_h1
            + r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * C2_pow_h2
        )
        + E1
        * (
            d1_pow_h1 * r1 * r2 * r1C1h1_pow_gamma21 * C2_pow_h2
            + d1_pow_h1 * r1 * r2 * r2C2h2_pow_gamma12 * C2_pow_h2
            + d1_pow_h1 * r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1_pow_gamma21 * r2 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
        )
        * (
            -d1_pow_h1 * r1 * r2 * r1C1h1_pow_gamma21 * C2_pow_h2 * h2
            - d1_pow_h1 * r1 * r2 * r2C2h2_pow_gamma12 * C2_pow_h2 * gamma12 * h2
            - d1_pow_h1 * r1 * r2 * r2C2h2_pow_gamma12 * C2_pow_h2 * h2
            - d1_pow_h1 * r1 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * C2_pow_h2 * h2
            - d1_pow_h1 * r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * gamma12 * h2
            - d2_pow_h2 * r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * gamma12 * h2
            - d2_pow_h2 * r1_pow_gamma21 * r2 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * gamma12 * h2
            - r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * C2_pow_h2 * h2
            - r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * C2_pow_h2 * gamma12 * h2
            - r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * C2_pow_h2 * h2
            - r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * C1_pow_h1 * gamma12 * h2
            - r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * C2_pow_h2 * h2
        )
        / (
            d1_pow_h1 * r1 * r2 * r1C1h1_pow_gamma21 * C2_pow_h2
            + d1_pow_h1 * r1 * r2 * r2C2h2_pow_gamma12 * C2_pow_h2
            + d1_pow_h1 * r1 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * C2_pow_h2
            + d1_pow_h1 * r1 * r2_pow_gamma12 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + d1_pow_h1 * r1_pow_gamma21p1 * r2_pow_gamma12 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
            + d1_pow_h1 * r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1
            + d2_pow_h2 * r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1
            + d2_pow_h2 * r1_pow_gamma21p1 * r2 * alpha21d1_pow_gamma21h1 * C1_pow_h1
            + d2_pow_h2 * r1_pow_gamma21 * r2 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1_pow_gamma21 * r2_pow_gamma12p1 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
            + d2_pow_h2 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * C2_pow_h2
            + r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * C2_pow_h2
            + r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * C1_pow_h1
            + r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * C2_pow_h2
        )
        ** 2
        + E1
        * (
            d1_pow_h1 * r1 * r2 * r1C1h1_pow_gamma21 * C2_pow_h2 * h2
            + d1_pow_h1 * r1 * r2 * r2C2h2_pow_gamma12 * C2_pow_h2 * gamma12 * h2
            + d1_pow_h1 * r1 * r2 * r2C2h2_pow_gamma12 * C2_pow_h2 * h2
            + d1_pow_h1 * r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * gamma12 * h2
            + d2_pow_h2 * r1_pow_gamma21 * r2 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * gamma12 * h2
        )
        / (
            d1_pow_h1 * r1 * r2 * r1C1h1_pow_gamma21 * C2_pow_h2
            + d1_pow_h1 * r1 * r2 * r2C2h2_pow_gamma12 * C2_pow_h2
            + d1_pow_h1 * r1 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * C2_pow_h2
            + d1_pow_h1 * r1 * r2_pow_gamma12 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + d1_pow_h1 * r1_pow_gamma21p1 * r2_pow_gamma12 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
            + d1_pow_h1 * r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1
            + d2_pow_h2 * r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1
            + d2_pow_h2 * r1_pow_gamma21p1 * r2 * alpha21d1_pow_gamma21h1 * C1_pow_h1
            + d2_pow_h2 * r1_pow_gamma21 * r2 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1_pow_gamma21 * r2_pow_gamma12p1 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
            + d2_pow_h2 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * C2_pow_h2
            + r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * C2_pow_h2
            + r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * C1_pow_h1
            + r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * C2_pow_h2
        )
        + E2
        * d2_pow_h2
        * r1
        * r2
        * r2C2h2_pow_gamma12
        * C1_pow_h1
        * gamma12
        * h2
        / (
            d1_pow_h1 * r1 * r2 * r1C1h1_pow_gamma21 * C2_pow_h2
            + d1_pow_h1 * r1 * r2 * r2C2h2_pow_gamma12 * C2_pow_h2
            + d1_pow_h1 * r1 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * C2_pow_h2
            + d1_pow_h1 * r1 * r2_pow_gamma12 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + d1_pow_h1 * r1_pow_gamma21p1 * r2_pow_gamma12 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
            + d1_pow_h1 * r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1
            + d2_pow_h2 * r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1
            + d2_pow_h2 * r1_pow_gamma21p1 * r2 * alpha21d1_pow_gamma21h1 * C1_pow_h1
            + d2_pow_h2 * r1_pow_gamma21 * r2 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1_pow_gamma21 * r2_pow_gamma12p1 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
            + d2_pow_h2 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * C2_pow_h2
            + r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * C2_pow_h2
            + r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * C1_pow_h1
            + r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * C2_pow_h2
        )
        + E2
        * (
            d1_pow_h1 * r1 * r2_pow_gamma12 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + d2_pow_h2 * r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1
            + d2_pow_h2 * r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1
            + d2_pow_h2 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
        )
        * (
            -d1_pow_h1 * r1 * r2 * r1C1h1_pow_gamma21 * C2_pow_h2 * h2
            - d1_pow_h1 * r1 * r2 * r2C2h2_pow_gamma12 * C2_pow_h2 * gamma12 * h2
            - d1_pow_h1 * r1 * r2 * r2C2h2_pow_gamma12 * C2_pow_h2 * h2
            - d1_pow_h1 * r1 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * C2_pow_h2 * h2
            - d1_pow_h1 * r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * gamma12 * h2
            - d2_pow_h2 * r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * gamma12 * h2
            - d2_pow_h2 * r1_pow_gamma21 * r2 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * gamma12 * h2
            - r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * C2_pow_h2 * h2
            - r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * C2_pow_h2 * gamma12 * h2
            - r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * C2_pow_h2 * h2
            - r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * C1_pow_h1 * gamma12 * h2
            - r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * C2_pow_h2 * h2
        )
        / (
            d1_pow_h1 * r1 * r2 * r1C1h1_pow_gamma21 * C2_pow_h2
            + d1_pow_h1 * r1 * r2 * r2C2h2_pow_gamma12 * C2_pow_h2
            + d1_pow_h1 * r1 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * C2_pow_h2
            + d1_pow_h1 * r1 * r2_pow_gamma12 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + d1_pow_h1 * r1_pow_gamma21p1 * r2_pow_gamma12 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
            + d1_pow_h1 * r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1
            + d2_pow_h2 * r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1
            + d2_pow_h2 * r1_pow_gamma21p1 * r2 * alpha21d1_pow_gamma21h1 * C1_pow_h1
            + d2_pow_h2 * r1_pow_gamma21 * r2 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1_pow_gamma21 * r2_pow_gamma12p1 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
            + d2_pow_h2 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * C2_pow_h2
            + r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * C2_pow_h2
            + r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * C1_pow_h1
            + r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * C2_pow_h2
        )
        ** 2
        + E3
        * (
            d2_pow_h2
            * r2**2
            * (r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            * (-d1_pow_h1 * r1 - r1 * C1_pow_h1 - r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            * C2_pow_h2
            * h2
            + r2
            * (
                d1_pow_h1 * r1 * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r1 * C1_pow_h1)
                - (d1_pow_h1 * r1 + d2_pow_h2 * r2)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
            * (-d1_pow_h1 * r1 - r1 * C1_pow_h1 - r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            * C2_pow_h2
            * h2
        )
        / (
            -(
                (-d1_pow_h1 * r1 + r2C2h2_pow_gamma12) * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r1 * C1_pow_h1)
                + (d1_pow_h1 * r1 + d2_pow_h2 * r2)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
            * (
                d1_pow_h1 * d2_pow_h2 * r1 * r2
                - (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
                * (d2_pow_h2 * r2 + r1_pow_gamma21 * alpha21d1_pow_gamma21h1 + r2 * C2_pow_h2)
            )
            + (
                d1_pow_h1 * r1 * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r1 * C1_pow_h1)
                - (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r2 * C2_pow_h2)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
            * (
                -d2_pow_h2 * r2 * (d1_pow_h1 * r1 - r2C2h2_pow_gamma12)
                + (d2_pow_h2 * r2 - r1C1h1_pow_gamma21)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
        )
        + E3
        * (
            d2_pow_h2
            * r2
            * (r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            * (
                d1_pow_h1 * r1 * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r1 * C1_pow_h1)
                - (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r2 * C2_pow_h2)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
            + (
                d1_pow_h1 * r1 * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r1 * C1_pow_h1)
                - (d1_pow_h1 * r1 + d2_pow_h2 * r2)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
            * (
                d1_pow_h1 * d2_pow_h2 * r1 * r2
                - (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
                * (d2_pow_h2 * r2 + r1_pow_gamma21 * alpha21d1_pow_gamma21h1 + r2 * C2_pow_h2)
            )
        )
        * (
            -d2_pow_h2
            * r2
            * r2C2h2_pow_gamma12
            * (
                d1_pow_h1 * r1 * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r1 * C1_pow_h1)
                - (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r2 * C2_pow_h2)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
            * gamma12
            * h2
            - r2
            * (
                -(-d1_pow_h1 * r1 + r2C2h2_pow_gamma12) * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r1 * C1_pow_h1)
                - (d1_pow_h1 * r1 + d2_pow_h2 * r2)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
            * (-d1_pow_h1 * r1 - r1 * C1_pow_h1 - r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            * C2_pow_h2
            * h2
            - r2
            * (
                -d2_pow_h2 * r2 * (d1_pow_h1 * r1 - r2C2h2_pow_gamma12)
                + (d2_pow_h2 * r2 - r1C1h1_pow_gamma21)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
            * (-d1_pow_h1 * r1 - r1 * C1_pow_h1 - r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            * C2_pow_h2
            * h2
            + r2C2h2_pow_gamma12
            * (
                d1_pow_h1 * d2_pow_h2 * r1 * r2
                - (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
                * (d2_pow_h2 * r2 + r1_pow_gamma21 * alpha21d1_pow_gamma21h1 + r2 * C2_pow_h2)
            )
            * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r1 * C1_pow_h1)
            * gamma12
            * h2
        )
        / (
            -(
                (-d1_pow_h1 * r1 + r2C2h2_pow_gamma12) * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r1 * C1_pow_h1)
                + (d1_pow_h1 * r1 + d2_pow_h2 * r2)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
            * (
                d1_pow_h1 * d2_pow_h2 * r1 * r2
                - (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
                * (d2_pow_h2 * r2 + r1_pow_gamma21 * alpha21d1_pow_gamma21h1 + r2 * C2_pow_h2)
            )
            + (
                d1_pow_h1 * r1 * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r1 * C1_pow_h1)
                - (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r2 * C2_pow_h2)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
            * (
                -d2_pow_h2 * r2 * (d1_pow_h1 * r1 - r2C2h2_pow_gamma12)
                + (d2_pow_h2 * r2 - r1C1h1_pow_gamma21)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
        )
        ** 2
    )

    # ********** logalpha12 ********

    j_logalpha12 = (
        E0
        * r2_pow_gamma12p1
        * alpha12d2_pow_gamma12h2
        * r1C1h1_pow_gamma21
        * C2_pow_h2
        * (gamma12 * h2)
        / (
            d1_pow_h1 * r1 * r2 * r1C1h1_pow_gamma21 * C2_pow_h2
            + d1_pow_h1 * r1 * r2 * r2C2h2_pow_gamma12 * C2_pow_h2
            + d1_pow_h1 * r1 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * C2_pow_h2
            + d1_pow_h1 * r1 * r2_pow_gamma12 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + d1_pow_h1 * r1_pow_gamma21p1 * r2_pow_gamma12 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
            + d1_pow_h1 * r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1
            + d2_pow_h2 * r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1
            + d2_pow_h2 * r1_pow_gamma21p1 * r2 * alpha21d1_pow_gamma21h1 * C1_pow_h1
            + d2_pow_h2 * r1_pow_gamma21 * r2 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1_pow_gamma21 * r2_pow_gamma12p1 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
            + d2_pow_h2 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * C2_pow_h2
            + r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * C2_pow_h2
            + r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * C1_pow_h1
            + r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * C2_pow_h2
        )
        + E0
        * (
            r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * C2_pow_h2
            + r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * C2_pow_h2
            + r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * C1_pow_h1
            + r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * C2_pow_h2
        )
        * (
            -d1_pow_h1 * r1 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * C2_pow_h2 * (gamma12 * h2)
            - d1_pow_h1 * r1 * r2_pow_gamma12 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * (gamma12 * h2)
            - d1_pow_h1
            * r1_pow_gamma21p1
            * r2_pow_gamma12
            * alpha21d1_pow_gamma21h1
            * alpha12d2_pow_gamma12h2
            * (gamma12 * h2)
            - d2_pow_h2
            * r1_pow_gamma21
            * r2_pow_gamma12p1
            * alpha21d1_pow_gamma21h1
            * alpha12d2_pow_gamma12h2
            * (gamma12 * h2)
            - d2_pow_h2 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * (gamma12 * h2)
            - r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * C2_pow_h2 * (gamma12 * h2)
        )
        / (
            d1_pow_h1 * r1 * r2 * r1C1h1_pow_gamma21 * C2_pow_h2
            + d1_pow_h1 * r1 * r2 * r2C2h2_pow_gamma12 * C2_pow_h2
            + d1_pow_h1 * r1 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * C2_pow_h2
            + d1_pow_h1 * r1 * r2_pow_gamma12 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + d1_pow_h1 * r1_pow_gamma21p1 * r2_pow_gamma12 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
            + d1_pow_h1 * r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1
            + d2_pow_h2 * r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1
            + d2_pow_h2 * r1_pow_gamma21p1 * r2 * alpha21d1_pow_gamma21h1 * C1_pow_h1
            + d2_pow_h2 * r1_pow_gamma21 * r2 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1_pow_gamma21 * r2_pow_gamma12p1 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
            + d2_pow_h2 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * C2_pow_h2
            + r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * C2_pow_h2
            + r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * C1_pow_h1
            + r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * C2_pow_h2
        )
        ** 2
        + E1
        * (
            d1_pow_h1 * r1 * r2 * r1C1h1_pow_gamma21 * C2_pow_h2
            + d1_pow_h1 * r1 * r2 * r2C2h2_pow_gamma12 * C2_pow_h2
            + d1_pow_h1 * r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1_pow_gamma21 * r2 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
        )
        * (
            -d1_pow_h1 * r1 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * C2_pow_h2 * (gamma12 * h2)
            - d1_pow_h1 * r1 * r2_pow_gamma12 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * (gamma12 * h2)
            - d1_pow_h1
            * r1_pow_gamma21p1
            * r2_pow_gamma12
            * alpha21d1_pow_gamma21h1
            * alpha12d2_pow_gamma12h2
            * (gamma12 * h2)
            - d2_pow_h2
            * r1_pow_gamma21
            * r2_pow_gamma12p1
            * alpha21d1_pow_gamma21h1
            * alpha12d2_pow_gamma12h2
            * (gamma12 * h2)
            - d2_pow_h2 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * (gamma12 * h2)
            - r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * C2_pow_h2 * (gamma12 * h2)
        )
        / (
            d1_pow_h1 * r1 * r2 * r1C1h1_pow_gamma21 * C2_pow_h2
            + d1_pow_h1 * r1 * r2 * r2C2h2_pow_gamma12 * C2_pow_h2
            + d1_pow_h1 * r1 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * C2_pow_h2
            + d1_pow_h1 * r1 * r2_pow_gamma12 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + d1_pow_h1 * r1_pow_gamma21p1 * r2_pow_gamma12 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
            + d1_pow_h1 * r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1
            + d2_pow_h2 * r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1
            + d2_pow_h2 * r1_pow_gamma21p1 * r2 * alpha21d1_pow_gamma21h1 * C1_pow_h1
            + d2_pow_h2 * r1_pow_gamma21 * r2 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1_pow_gamma21 * r2_pow_gamma12p1 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
            + d2_pow_h2 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * C2_pow_h2
            + r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * C2_pow_h2
            + r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * C1_pow_h1
            + r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * C2_pow_h2
        )
        ** 2
        + E2
        * (
            d1_pow_h1 * r1 * r2_pow_gamma12 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * (gamma12 * h2)
            + d2_pow_h2 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * (gamma12 * h2)
        )
        / (
            d1_pow_h1 * r1 * r2 * r1C1h1_pow_gamma21 * C2_pow_h2
            + d1_pow_h1 * r1 * r2 * r2C2h2_pow_gamma12 * C2_pow_h2
            + d1_pow_h1 * r1 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * C2_pow_h2
            + d1_pow_h1 * r1 * r2_pow_gamma12 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + d1_pow_h1 * r1_pow_gamma21p1 * r2_pow_gamma12 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
            + d1_pow_h1 * r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1
            + d2_pow_h2 * r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1
            + d2_pow_h2 * r1_pow_gamma21p1 * r2 * alpha21d1_pow_gamma21h1 * C1_pow_h1
            + d2_pow_h2 * r1_pow_gamma21 * r2 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1_pow_gamma21 * r2_pow_gamma12p1 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
            + d2_pow_h2 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * C2_pow_h2
            + r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * C2_pow_h2
            + r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * C1_pow_h1
            + r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * C2_pow_h2
        )
        + E2
        * (
            d1_pow_h1 * r1 * r2_pow_gamma12 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + d2_pow_h2 * r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1
            + d2_pow_h2 * r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1
            + d2_pow_h2 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
        )
        * (
            -d1_pow_h1 * r1 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * C2_pow_h2 * (gamma12 * h2)
            - d1_pow_h1 * r1 * r2_pow_gamma12 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * (gamma12 * h2)
            - d1_pow_h1
            * r1_pow_gamma21p1
            * r2_pow_gamma12
            * alpha21d1_pow_gamma21h1
            * alpha12d2_pow_gamma12h2
            * (gamma12 * h2)
            - d2_pow_h2
            * r1_pow_gamma21
            * r2_pow_gamma12p1
            * alpha21d1_pow_gamma21h1
            * alpha12d2_pow_gamma12h2
            * (gamma12 * h2)
            - d2_pow_h2 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * (gamma12 * h2)
            - r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * C2_pow_h2 * (gamma12 * h2)
        )
        / (
            d1_pow_h1 * r1 * r2 * r1C1h1_pow_gamma21 * C2_pow_h2
            + d1_pow_h1 * r1 * r2 * r2C2h2_pow_gamma12 * C2_pow_h2
            + d1_pow_h1 * r1 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * C2_pow_h2
            + d1_pow_h1 * r1 * r2_pow_gamma12 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + d1_pow_h1 * r1_pow_gamma21p1 * r2_pow_gamma12 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
            + d1_pow_h1 * r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1
            + d2_pow_h2 * r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1
            + d2_pow_h2 * r1_pow_gamma21p1 * r2 * alpha21d1_pow_gamma21h1 * C1_pow_h1
            + d2_pow_h2 * r1_pow_gamma21 * r2 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1_pow_gamma21 * r2_pow_gamma12p1 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
            + d2_pow_h2 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * C2_pow_h2
            + r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * C2_pow_h2
            + r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * C1_pow_h1
            + r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * C2_pow_h2
        )
        ** 2
        + E3
        * (
            -d2_pow_h2
            * r2
            * r2_pow_gamma12
            * alpha12d2_pow_gamma12h2
            * (r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r2 * C2_pow_h2)
            * (gamma12 * h2)
            + d2_pow_h2
            * r2
            * r2_pow_gamma12
            * alpha12d2_pow_gamma12h2
            * (
                d1_pow_h1 * r1 * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r1 * C1_pow_h1)
                - (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r2 * C2_pow_h2)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
            * (gamma12 * h2)
            + r2_pow_gamma12
            * alpha12d2_pow_gamma12h2
            * (-d1_pow_h1 * r1 - d2_pow_h2 * r2)
            * (
                d1_pow_h1 * d2_pow_h2 * r1 * r2
                - (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
                * (d2_pow_h2 * r2 + r1_pow_gamma21 * alpha21d1_pow_gamma21h1 + r2 * C2_pow_h2)
            )
            * (gamma12 * h2)
            - r2_pow_gamma12
            * alpha12d2_pow_gamma12h2
            * (
                d1_pow_h1 * r1 * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r1 * C1_pow_h1)
                - (d1_pow_h1 * r1 + d2_pow_h2 * r2)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
            * (d2_pow_h2 * r2 + r1_pow_gamma21 * alpha21d1_pow_gamma21h1 + r2 * C2_pow_h2)
            * (gamma12 * h2)
        )
        / (
            -(
                (-d1_pow_h1 * r1 + r2C2h2_pow_gamma12) * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r1 * C1_pow_h1)
                + (d1_pow_h1 * r1 + d2_pow_h2 * r2)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
            * (
                d1_pow_h1 * d2_pow_h2 * r1 * r2
                - (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
                * (d2_pow_h2 * r2 + r1_pow_gamma21 * alpha21d1_pow_gamma21h1 + r2 * C2_pow_h2)
            )
            + (
                d1_pow_h1 * r1 * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r1 * C1_pow_h1)
                - (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r2 * C2_pow_h2)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
            * (
                -d2_pow_h2 * r2 * (d1_pow_h1 * r1 - r2C2h2_pow_gamma12)
                + (d2_pow_h2 * r2 - r1C1h1_pow_gamma21)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
        )
        + E3
        * (
            d2_pow_h2
            * r2
            * (r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            * (
                d1_pow_h1 * r1 * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r1 * C1_pow_h1)
                - (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r2 * C2_pow_h2)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
            + (
                d1_pow_h1 * r1 * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r1 * C1_pow_h1)
                - (d1_pow_h1 * r1 + d2_pow_h2 * r2)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
            * (
                d1_pow_h1 * d2_pow_h2 * r1 * r2
                - (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
                * (d2_pow_h2 * r2 + r1_pow_gamma21 * alpha21d1_pow_gamma21h1 + r2 * C2_pow_h2)
            )
        )
        * (
            r2_pow_gamma12
            * alpha12d2_pow_gamma12h2
            * (d1_pow_h1 * r1 + d2_pow_h2 * r2)
            * (
                d1_pow_h1 * d2_pow_h2 * r1 * r2
                - (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
                * (d2_pow_h2 * r2 + r1_pow_gamma21 * alpha21d1_pow_gamma21h1 + r2 * C2_pow_h2)
            )
            * (gamma12 * h2)
            - r2_pow_gamma12
            * alpha12d2_pow_gamma12h2
            * (d2_pow_h2 * r2 - r1C1h1_pow_gamma21)
            * (
                d1_pow_h1 * r1 * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r1 * C1_pow_h1)
                - (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r2 * C2_pow_h2)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
            * (gamma12 * h2)
            + r2_pow_gamma12
            * alpha12d2_pow_gamma12h2
            * (
                -(-d1_pow_h1 * r1 + r2C2h2_pow_gamma12) * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r1 * C1_pow_h1)
                - (d1_pow_h1 * r1 + d2_pow_h2 * r2)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
            * (d2_pow_h2 * r2 + r1_pow_gamma21 * alpha21d1_pow_gamma21h1 + r2 * C2_pow_h2)
            * (gamma12 * h2)
            + r2_pow_gamma12
            * alpha12d2_pow_gamma12h2
            * (
                -d2_pow_h2 * r2 * (d1_pow_h1 * r1 - r2C2h2_pow_gamma12)
                + (d2_pow_h2 * r2 - r1C1h1_pow_gamma21)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
            * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r2 * C2_pow_h2)
            * (gamma12 * h2)
        )
        / (
            -(
                (-d1_pow_h1 * r1 + r2C2h2_pow_gamma12) * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r1 * C1_pow_h1)
                + (d1_pow_h1 * r1 + d2_pow_h2 * r2)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
            * (
                d1_pow_h1 * d2_pow_h2 * r1 * r2
                - (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
                * (d2_pow_h2 * r2 + r1_pow_gamma21 * alpha21d1_pow_gamma21h1 + r2 * C2_pow_h2)
            )
            + (
                d1_pow_h1 * r1 * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r1 * C1_pow_h1)
                - (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r2 * C2_pow_h2)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
            * (
                -d2_pow_h2 * r2 * (d1_pow_h1 * r1 - r2C2h2_pow_gamma12)
                + (d2_pow_h2 * r2 - r1C1h1_pow_gamma21)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
        )
        ** 2
    )

    # ********** logalpha21 ********

    j_logalpha21 = (
        E0
        * r1_pow_gamma21p1
        * alpha21d1_pow_gamma21h1
        * r2C2h2_pow_gamma12
        * C1_pow_h1
        * (gamma21 * h1)
        / (
            d1_pow_h1 * r1 * r2 * r1C1h1_pow_gamma21 * C2_pow_h2
            + d1_pow_h1 * r1 * r2 * r2C2h2_pow_gamma12 * C2_pow_h2
            + d1_pow_h1 * r1 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * C2_pow_h2
            + d1_pow_h1 * r1 * r2_pow_gamma12 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + d1_pow_h1 * r1_pow_gamma21p1 * r2_pow_gamma12 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
            + d1_pow_h1 * r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1
            + d2_pow_h2 * r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1
            + d2_pow_h2 * r1_pow_gamma21p1 * r2 * alpha21d1_pow_gamma21h1 * C1_pow_h1
            + d2_pow_h2 * r1_pow_gamma21 * r2 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1_pow_gamma21 * r2_pow_gamma12p1 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
            + d2_pow_h2 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * C2_pow_h2
            + r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * C2_pow_h2
            + r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * C1_pow_h1
            + r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * C2_pow_h2
        )
        + E0
        * (
            r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * C2_pow_h2
            + r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * C2_pow_h2
            + r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * C1_pow_h1
            + r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * C2_pow_h2
        )
        * (
            -d1_pow_h1
            * r1_pow_gamma21p1
            * r2_pow_gamma12
            * alpha21d1_pow_gamma21h1
            * alpha12d2_pow_gamma12h2
            * (gamma21 * h1)
            - d1_pow_h1 * r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * (gamma21 * h1)
            - d2_pow_h2 * r1_pow_gamma21p1 * r2 * alpha21d1_pow_gamma21h1 * C1_pow_h1 * (gamma21 * h1)
            - d2_pow_h2 * r1_pow_gamma21 * r2 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * (gamma21 * h1)
            - d2_pow_h2
            * r1_pow_gamma21
            * r2_pow_gamma12p1
            * alpha21d1_pow_gamma21h1
            * alpha12d2_pow_gamma12h2
            * (gamma21 * h1)
            - r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * C1_pow_h1 * (gamma21 * h1)
        )
        / (
            d1_pow_h1 * r1 * r2 * r1C1h1_pow_gamma21 * C2_pow_h2
            + d1_pow_h1 * r1 * r2 * r2C2h2_pow_gamma12 * C2_pow_h2
            + d1_pow_h1 * r1 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * C2_pow_h2
            + d1_pow_h1 * r1 * r2_pow_gamma12 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + d1_pow_h1 * r1_pow_gamma21p1 * r2_pow_gamma12 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
            + d1_pow_h1 * r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1
            + d2_pow_h2 * r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1
            + d2_pow_h2 * r1_pow_gamma21p1 * r2 * alpha21d1_pow_gamma21h1 * C1_pow_h1
            + d2_pow_h2 * r1_pow_gamma21 * r2 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1_pow_gamma21 * r2_pow_gamma12p1 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
            + d2_pow_h2 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * C2_pow_h2
            + r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * C2_pow_h2
            + r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * C1_pow_h1
            + r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * C2_pow_h2
        )
        ** 2
        + E1
        * (
            d1_pow_h1 * r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * (gamma21 * h1)
            + d2_pow_h2 * r1_pow_gamma21 * r2 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * (gamma21 * h1)
        )
        / (
            d1_pow_h1 * r1 * r2 * r1C1h1_pow_gamma21 * C2_pow_h2
            + d1_pow_h1 * r1 * r2 * r2C2h2_pow_gamma12 * C2_pow_h2
            + d1_pow_h1 * r1 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * C2_pow_h2
            + d1_pow_h1 * r1 * r2_pow_gamma12 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + d1_pow_h1 * r1_pow_gamma21p1 * r2_pow_gamma12 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
            + d1_pow_h1 * r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1
            + d2_pow_h2 * r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1
            + d2_pow_h2 * r1_pow_gamma21p1 * r2 * alpha21d1_pow_gamma21h1 * C1_pow_h1
            + d2_pow_h2 * r1_pow_gamma21 * r2 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1_pow_gamma21 * r2_pow_gamma12p1 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
            + d2_pow_h2 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * C2_pow_h2
            + r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * C2_pow_h2
            + r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * C1_pow_h1
            + r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * C2_pow_h2
        )
        + E1
        * (
            d1_pow_h1 * r1 * r2 * r1C1h1_pow_gamma21 * C2_pow_h2
            + d1_pow_h1 * r1 * r2 * r2C2h2_pow_gamma12 * C2_pow_h2
            + d1_pow_h1 * r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1_pow_gamma21 * r2 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
        )
        * (
            -d1_pow_h1
            * r1_pow_gamma21p1
            * r2_pow_gamma12
            * alpha21d1_pow_gamma21h1
            * alpha12d2_pow_gamma12h2
            * (gamma21 * h1)
            - d1_pow_h1 * r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * (gamma21 * h1)
            - d2_pow_h2 * r1_pow_gamma21p1 * r2 * alpha21d1_pow_gamma21h1 * C1_pow_h1 * (gamma21 * h1)
            - d2_pow_h2 * r1_pow_gamma21 * r2 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * (gamma21 * h1)
            - d2_pow_h2
            * r1_pow_gamma21
            * r2_pow_gamma12p1
            * alpha21d1_pow_gamma21h1
            * alpha12d2_pow_gamma12h2
            * (gamma21 * h1)
            - r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * C1_pow_h1 * (gamma21 * h1)
        )
        / (
            d1_pow_h1 * r1 * r2 * r1C1h1_pow_gamma21 * C2_pow_h2
            + d1_pow_h1 * r1 * r2 * r2C2h2_pow_gamma12 * C2_pow_h2
            + d1_pow_h1 * r1 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * C2_pow_h2
            + d1_pow_h1 * r1 * r2_pow_gamma12 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + d1_pow_h1 * r1_pow_gamma21p1 * r2_pow_gamma12 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
            + d1_pow_h1 * r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1
            + d2_pow_h2 * r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1
            + d2_pow_h2 * r1_pow_gamma21p1 * r2 * alpha21d1_pow_gamma21h1 * C1_pow_h1
            + d2_pow_h2 * r1_pow_gamma21 * r2 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1_pow_gamma21 * r2_pow_gamma12p1 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
            + d2_pow_h2 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * C2_pow_h2
            + r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * C2_pow_h2
            + r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * C1_pow_h1
            + r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * C2_pow_h2
        )
        ** 2
        + E2
        * (
            d1_pow_h1 * r1 * r2_pow_gamma12 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + d2_pow_h2 * r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1
            + d2_pow_h2 * r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1
            + d2_pow_h2 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
        )
        * (
            -d1_pow_h1
            * r1_pow_gamma21p1
            * r2_pow_gamma12
            * alpha21d1_pow_gamma21h1
            * alpha12d2_pow_gamma12h2
            * (gamma21 * h1)
            - d1_pow_h1 * r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * (gamma21 * h1)
            - d2_pow_h2 * r1_pow_gamma21p1 * r2 * alpha21d1_pow_gamma21h1 * C1_pow_h1 * (gamma21 * h1)
            - d2_pow_h2 * r1_pow_gamma21 * r2 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * (gamma21 * h1)
            - d2_pow_h2
            * r1_pow_gamma21
            * r2_pow_gamma12p1
            * alpha21d1_pow_gamma21h1
            * alpha12d2_pow_gamma12h2
            * (gamma21 * h1)
            - r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * C1_pow_h1 * (gamma21 * h1)
        )
        / (
            d1_pow_h1 * r1 * r2 * r1C1h1_pow_gamma21 * C2_pow_h2
            + d1_pow_h1 * r1 * r2 * r2C2h2_pow_gamma12 * C2_pow_h2
            + d1_pow_h1 * r1 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * C2_pow_h2
            + d1_pow_h1 * r1 * r2_pow_gamma12 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + d1_pow_h1 * r1_pow_gamma21p1 * r2_pow_gamma12 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
            + d1_pow_h1 * r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1
            + d2_pow_h2 * r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1
            + d2_pow_h2 * r1_pow_gamma21p1 * r2 * alpha21d1_pow_gamma21h1 * C1_pow_h1
            + d2_pow_h2 * r1_pow_gamma21 * r2 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1_pow_gamma21 * r2_pow_gamma12p1 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
            + d2_pow_h2 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * C2_pow_h2
            + r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * C2_pow_h2
            + r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * C1_pow_h1
            + r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * C2_pow_h2
        )
        ** 2
        - E3
        * r1_pow_gamma21
        * alpha21d1_pow_gamma21h1
        * (
            -(-d1_pow_h1 * r1 + r2C2h2_pow_gamma12) * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r1 * C1_pow_h1)
            - (d1_pow_h1 * r1 + d2_pow_h2 * r2)
            * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
        )
        * (
            d2_pow_h2
            * r2
            * (r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            * (
                d1_pow_h1 * r1 * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r1 * C1_pow_h1)
                - (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r2 * C2_pow_h2)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
            + (
                d1_pow_h1 * r1 * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r1 * C1_pow_h1)
                - (d1_pow_h1 * r1 + d2_pow_h2 * r2)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
            * (
                d1_pow_h1 * d2_pow_h2 * r1 * r2
                - (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
                * (d2_pow_h2 * r2 + r1_pow_gamma21 * alpha21d1_pow_gamma21h1 + r2 * C2_pow_h2)
            )
        )
        * (-d1_pow_h1 * r1 - r1 * C1_pow_h1 - r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
        * (gamma21 * h1)
        / (
            -(
                (-d1_pow_h1 * r1 + r2C2h2_pow_gamma12) * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r1 * C1_pow_h1)
                + (d1_pow_h1 * r1 + d2_pow_h2 * r2)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
            * (
                d1_pow_h1 * d2_pow_h2 * r1 * r2
                - (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
                * (d2_pow_h2 * r2 + r1_pow_gamma21 * alpha21d1_pow_gamma21h1 + r2 * C2_pow_h2)
            )
            + (
                d1_pow_h1 * r1 * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r1 * C1_pow_h1)
                - (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r2 * C2_pow_h2)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
            * (
                -d2_pow_h2 * r2 * (d1_pow_h1 * r1 - r2C2h2_pow_gamma12)
                + (d2_pow_h2 * r2 - r1C1h1_pow_gamma21)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
        )
        ** 2
        + E3
        * r1_pow_gamma21
        * alpha21d1_pow_gamma21h1
        * (
            d1_pow_h1 * r1 * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r1 * C1_pow_h1)
            - (d1_pow_h1 * r1 + d2_pow_h2 * r2)
            * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
        )
        * (-d1_pow_h1 * r1 - r1 * C1_pow_h1 - r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
        * (gamma21 * h1)
        / (
            -(
                (-d1_pow_h1 * r1 + r2C2h2_pow_gamma12) * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r1 * C1_pow_h1)
                + (d1_pow_h1 * r1 + d2_pow_h2 * r2)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
            * (
                d1_pow_h1 * d2_pow_h2 * r1 * r2
                - (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
                * (d2_pow_h2 * r2 + r1_pow_gamma21 * alpha21d1_pow_gamma21h1 + r2 * C2_pow_h2)
            )
            + (
                d1_pow_h1 * r1 * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r1 * C1_pow_h1)
                - (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r2 * C2_pow_h2)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
            * (
                -d2_pow_h2 * r2 * (d1_pow_h1 * r1 - r2C2h2_pow_gamma12)
                + (d2_pow_h2 * r2 - r1C1h1_pow_gamma21)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
        )
    )

    # ********** loggamma12 ********

    j_loggamma12 = (
        E0
        * (
            r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * C2_pow_h2
            + r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * C2_pow_h2
            + r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * C1_pow_h1
            + r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * C2_pow_h2
        )
        * (
            -d1_pow_h1 * r1 * r2 * r2C2h2_pow_gamma12 * C2_pow_h2 * gamma12 * log(r2 * C2_pow_h2)
            - d1_pow_h1 * r1 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * C2_pow_h2 * gamma12 * log(r2)
            - d1_pow_h1 * r1 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * C2_pow_h2 * (gamma12 * h2) * logd2alpha12
            - d1_pow_h1 * r1 * r2_pow_gamma12 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * gamma12 * log(r2)
            - d1_pow_h1
            * r1
            * r2_pow_gamma12
            * alpha12d2_pow_gamma12h2
            * r1C1h1_pow_gamma21
            * (gamma12 * h2)
            * logd2alpha12
            - d1_pow_h1
            * r1_pow_gamma21p1
            * r2_pow_gamma12
            * alpha21d1_pow_gamma21h1
            * alpha12d2_pow_gamma12h2
            * gamma12
            * log(r2)
            - d1_pow_h1
            * r1_pow_gamma21p1
            * r2_pow_gamma12
            * alpha21d1_pow_gamma21h1
            * alpha12d2_pow_gamma12h2
            * (gamma12 * h2)
            * logd2alpha12
            - d1_pow_h1
            * r1_pow_gamma21p1
            * alpha21d1_pow_gamma21h1
            * r2C2h2_pow_gamma12
            * gamma12
            * log(r2 * C2_pow_h2)
            - d2_pow_h2 * r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * gamma12 * log(r2 * C2_pow_h2)
            - d2_pow_h2
            * r1_pow_gamma21
            * r2
            * alpha21d1_pow_gamma21h1
            * r2C2h2_pow_gamma12
            * gamma12
            * log(r2 * C2_pow_h2)
            - d2_pow_h2
            * r1_pow_gamma21
            * r2_pow_gamma12p1
            * alpha21d1_pow_gamma21h1
            * alpha12d2_pow_gamma12h2
            * gamma12
            * log(r2)
            - d2_pow_h2
            * r1_pow_gamma21
            * r2_pow_gamma12p1
            * alpha21d1_pow_gamma21h1
            * alpha12d2_pow_gamma12h2
            * (gamma12 * h2)
            * logd2alpha12
            - d2_pow_h2 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * gamma12 * log(r2)
            - d2_pow_h2
            * r2_pow_gamma12p1
            * alpha12d2_pow_gamma12h2
            * r1C1h1_pow_gamma21
            * (gamma12 * h2)
            * logd2alpha12
            - r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * C2_pow_h2 * gamma12 * log(r2 * C2_pow_h2)
            - r1_pow_gamma21p1
            * alpha21d1_pow_gamma21h1
            * r2C2h2_pow_gamma12
            * C1_pow_h1
            * gamma12
            * log(r2 * C2_pow_h2)
            - r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * C2_pow_h2 * gamma12 * log(r2)
            - r2_pow_gamma12p1
            * alpha12d2_pow_gamma12h2
            * r1C1h1_pow_gamma21
            * C2_pow_h2
            * (gamma12 * h2)
            * logd2alpha12
        )
        / (
            d1_pow_h1 * r1 * r2 * r1C1h1_pow_gamma21 * C2_pow_h2
            + d1_pow_h1 * r1 * r2 * r2C2h2_pow_gamma12 * C2_pow_h2
            + d1_pow_h1 * r1 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * C2_pow_h2
            + d1_pow_h1 * r1 * r2_pow_gamma12 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + d1_pow_h1 * r1_pow_gamma21p1 * r2_pow_gamma12 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
            + d1_pow_h1 * r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1
            + d2_pow_h2 * r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1
            + d2_pow_h2 * r1_pow_gamma21p1 * r2 * alpha21d1_pow_gamma21h1 * C1_pow_h1
            + d2_pow_h2 * r1_pow_gamma21 * r2 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1_pow_gamma21 * r2_pow_gamma12p1 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
            + d2_pow_h2 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * C2_pow_h2
            + r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * C2_pow_h2
            + r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * C1_pow_h1
            + r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * C2_pow_h2
        )
        ** 2
        + E0
        * (
            r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * C2_pow_h2 * gamma12 * log(r2 * C2_pow_h2)
            + r1_pow_gamma21p1
            * alpha21d1_pow_gamma21h1
            * r2C2h2_pow_gamma12
            * C1_pow_h1
            * gamma12
            * log(r2 * C2_pow_h2)
            + r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * C2_pow_h2 * gamma12 * log(r2)
            + r2_pow_gamma12p1
            * alpha12d2_pow_gamma12h2
            * r1C1h1_pow_gamma21
            * C2_pow_h2
            * (gamma12 * h2)
            * logd2alpha12
        )
        / (
            d1_pow_h1 * r1 * r2 * r1C1h1_pow_gamma21 * C2_pow_h2
            + d1_pow_h1 * r1 * r2 * r2C2h2_pow_gamma12 * C2_pow_h2
            + d1_pow_h1 * r1 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * C2_pow_h2
            + d1_pow_h1 * r1 * r2_pow_gamma12 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + d1_pow_h1 * r1_pow_gamma21p1 * r2_pow_gamma12 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
            + d1_pow_h1 * r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1
            + d2_pow_h2 * r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1
            + d2_pow_h2 * r1_pow_gamma21p1 * r2 * alpha21d1_pow_gamma21h1 * C1_pow_h1
            + d2_pow_h2 * r1_pow_gamma21 * r2 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1_pow_gamma21 * r2_pow_gamma12p1 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
            + d2_pow_h2 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * C2_pow_h2
            + r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * C2_pow_h2
            + r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * C1_pow_h1
            + r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * C2_pow_h2
        )
        + E1
        * (
            d1_pow_h1 * r1 * r2 * r2C2h2_pow_gamma12 * C2_pow_h2 * gamma12 * log(r2 * C2_pow_h2)
            + d1_pow_h1
            * r1_pow_gamma21p1
            * alpha21d1_pow_gamma21h1
            * r2C2h2_pow_gamma12
            * gamma12
            * log(r2 * C2_pow_h2)
            + d2_pow_h2
            * r1_pow_gamma21
            * r2
            * alpha21d1_pow_gamma21h1
            * r2C2h2_pow_gamma12
            * gamma12
            * log(r2 * C2_pow_h2)
        )
        / (
            d1_pow_h1 * r1 * r2 * r1C1h1_pow_gamma21 * C2_pow_h2
            + d1_pow_h1 * r1 * r2 * r2C2h2_pow_gamma12 * C2_pow_h2
            + d1_pow_h1 * r1 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * C2_pow_h2
            + d1_pow_h1 * r1 * r2_pow_gamma12 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + d1_pow_h1 * r1_pow_gamma21p1 * r2_pow_gamma12 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
            + d1_pow_h1 * r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1
            + d2_pow_h2 * r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1
            + d2_pow_h2 * r1_pow_gamma21p1 * r2 * alpha21d1_pow_gamma21h1 * C1_pow_h1
            + d2_pow_h2 * r1_pow_gamma21 * r2 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1_pow_gamma21 * r2_pow_gamma12p1 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
            + d2_pow_h2 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * C2_pow_h2
            + r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * C2_pow_h2
            + r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * C1_pow_h1
            + r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * C2_pow_h2
        )
        + E1
        * (
            d1_pow_h1 * r1 * r2 * r1C1h1_pow_gamma21 * C2_pow_h2
            + d1_pow_h1 * r1 * r2 * r2C2h2_pow_gamma12 * C2_pow_h2
            + d1_pow_h1 * r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1_pow_gamma21 * r2 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
        )
        * (
            -d1_pow_h1 * r1 * r2 * r2C2h2_pow_gamma12 * C2_pow_h2 * gamma12 * log(r2 * C2_pow_h2)
            - d1_pow_h1 * r1 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * C2_pow_h2 * gamma12 * log(r2)
            - d1_pow_h1 * r1 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * C2_pow_h2 * (gamma12 * h2) * logd2alpha12
            - d1_pow_h1 * r1 * r2_pow_gamma12 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * gamma12 * log(r2)
            - d1_pow_h1
            * r1
            * r2_pow_gamma12
            * alpha12d2_pow_gamma12h2
            * r1C1h1_pow_gamma21
            * (gamma12 * h2)
            * logd2alpha12
            - d1_pow_h1
            * r1_pow_gamma21p1
            * r2_pow_gamma12
            * alpha21d1_pow_gamma21h1
            * alpha12d2_pow_gamma12h2
            * gamma12
            * log(r2)
            - d1_pow_h1
            * r1_pow_gamma21p1
            * r2_pow_gamma12
            * alpha21d1_pow_gamma21h1
            * alpha12d2_pow_gamma12h2
            * (gamma12 * h2)
            * logd2alpha12
            - d1_pow_h1
            * r1_pow_gamma21p1
            * alpha21d1_pow_gamma21h1
            * r2C2h2_pow_gamma12
            * gamma12
            * log(r2 * C2_pow_h2)
            - d2_pow_h2 * r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * gamma12 * log(r2 * C2_pow_h2)
            - d2_pow_h2
            * r1_pow_gamma21
            * r2
            * alpha21d1_pow_gamma21h1
            * r2C2h2_pow_gamma12
            * gamma12
            * log(r2 * C2_pow_h2)
            - d2_pow_h2
            * r1_pow_gamma21
            * r2_pow_gamma12p1
            * alpha21d1_pow_gamma21h1
            * alpha12d2_pow_gamma12h2
            * gamma12
            * log(r2)
            - d2_pow_h2
            * r1_pow_gamma21
            * r2_pow_gamma12p1
            * alpha21d1_pow_gamma21h1
            * alpha12d2_pow_gamma12h2
            * (gamma12 * h2)
            * logd2alpha12
            - d2_pow_h2 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * gamma12 * log(r2)
            - d2_pow_h2
            * r2_pow_gamma12p1
            * alpha12d2_pow_gamma12h2
            * r1C1h1_pow_gamma21
            * (gamma12 * h2)
            * logd2alpha12
            - r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * C2_pow_h2 * gamma12 * log(r2 * C2_pow_h2)
            - r1_pow_gamma21p1
            * alpha21d1_pow_gamma21h1
            * r2C2h2_pow_gamma12
            * C1_pow_h1
            * gamma12
            * log(r2 * C2_pow_h2)
            - r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * C2_pow_h2 * gamma12 * log(r2)
            - r2_pow_gamma12p1
            * alpha12d2_pow_gamma12h2
            * r1C1h1_pow_gamma21
            * C2_pow_h2
            * (gamma12 * h2)
            * logd2alpha12
        )
        / (
            d1_pow_h1 * r1 * r2 * r1C1h1_pow_gamma21 * C2_pow_h2
            + d1_pow_h1 * r1 * r2 * r2C2h2_pow_gamma12 * C2_pow_h2
            + d1_pow_h1 * r1 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * C2_pow_h2
            + d1_pow_h1 * r1 * r2_pow_gamma12 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + d1_pow_h1 * r1_pow_gamma21p1 * r2_pow_gamma12 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
            + d1_pow_h1 * r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1
            + d2_pow_h2 * r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1
            + d2_pow_h2 * r1_pow_gamma21p1 * r2 * alpha21d1_pow_gamma21h1 * C1_pow_h1
            + d2_pow_h2 * r1_pow_gamma21 * r2 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1_pow_gamma21 * r2_pow_gamma12p1 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
            + d2_pow_h2 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * C2_pow_h2
            + r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * C2_pow_h2
            + r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * C1_pow_h1
            + r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * C2_pow_h2
        )
        ** 2
        + E2
        * (
            d1_pow_h1 * r1 * r2_pow_gamma12 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + d2_pow_h2 * r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1
            + d2_pow_h2 * r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1
            + d2_pow_h2 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
        )
        * (
            -d1_pow_h1 * r1 * r2 * r2C2h2_pow_gamma12 * C2_pow_h2 * gamma12 * log(r2 * C2_pow_h2)
            - d1_pow_h1 * r1 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * C2_pow_h2 * gamma12 * log(r2)
            - d1_pow_h1 * r1 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * C2_pow_h2 * (gamma12 * h2) * logd2alpha12
            - d1_pow_h1 * r1 * r2_pow_gamma12 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * gamma12 * log(r2)
            - d1_pow_h1
            * r1
            * r2_pow_gamma12
            * alpha12d2_pow_gamma12h2
            * r1C1h1_pow_gamma21
            * (gamma12 * h2)
            * logd2alpha12
            - d1_pow_h1
            * r1_pow_gamma21p1
            * r2_pow_gamma12
            * alpha21d1_pow_gamma21h1
            * alpha12d2_pow_gamma12h2
            * gamma12
            * log(r2)
            - d1_pow_h1
            * r1_pow_gamma21p1
            * r2_pow_gamma12
            * alpha21d1_pow_gamma21h1
            * alpha12d2_pow_gamma12h2
            * (gamma12 * h2)
            * logd2alpha12
            - d1_pow_h1
            * r1_pow_gamma21p1
            * alpha21d1_pow_gamma21h1
            * r2C2h2_pow_gamma12
            * gamma12
            * log(r2 * C2_pow_h2)
            - d2_pow_h2 * r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * gamma12 * log(r2 * C2_pow_h2)
            - d2_pow_h2
            * r1_pow_gamma21
            * r2
            * alpha21d1_pow_gamma21h1
            * r2C2h2_pow_gamma12
            * gamma12
            * log(r2 * C2_pow_h2)
            - d2_pow_h2
            * r1_pow_gamma21
            * r2_pow_gamma12p1
            * alpha21d1_pow_gamma21h1
            * alpha12d2_pow_gamma12h2
            * gamma12
            * log(r2)
            - d2_pow_h2
            * r1_pow_gamma21
            * r2_pow_gamma12p1
            * alpha21d1_pow_gamma21h1
            * alpha12d2_pow_gamma12h2
            * (gamma12 * h2)
            * logd2alpha12
            - d2_pow_h2 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * gamma12 * log(r2)
            - d2_pow_h2
            * r2_pow_gamma12p1
            * alpha12d2_pow_gamma12h2
            * r1C1h1_pow_gamma21
            * (gamma12 * h2)
            * logd2alpha12
            - r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * C2_pow_h2 * gamma12 * log(r2 * C2_pow_h2)
            - r1_pow_gamma21p1
            * alpha21d1_pow_gamma21h1
            * r2C2h2_pow_gamma12
            * C1_pow_h1
            * gamma12
            * log(r2 * C2_pow_h2)
            - r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * C2_pow_h2 * gamma12 * log(r2)
            - r2_pow_gamma12p1
            * alpha12d2_pow_gamma12h2
            * r1C1h1_pow_gamma21
            * C2_pow_h2
            * (gamma12 * h2)
            * logd2alpha12
        )
        / (
            d1_pow_h1 * r1 * r2 * r1C1h1_pow_gamma21 * C2_pow_h2
            + d1_pow_h1 * r1 * r2 * r2C2h2_pow_gamma12 * C2_pow_h2
            + d1_pow_h1 * r1 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * C2_pow_h2
            + d1_pow_h1 * r1 * r2_pow_gamma12 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + d1_pow_h1 * r1_pow_gamma21p1 * r2_pow_gamma12 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
            + d1_pow_h1 * r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1
            + d2_pow_h2 * r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1
            + d2_pow_h2 * r1_pow_gamma21p1 * r2 * alpha21d1_pow_gamma21h1 * C1_pow_h1
            + d2_pow_h2 * r1_pow_gamma21 * r2 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1_pow_gamma21 * r2_pow_gamma12p1 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
            + d2_pow_h2 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * C2_pow_h2
            + r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * C2_pow_h2
            + r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * C1_pow_h1
            + r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * C2_pow_h2
        )
        ** 2
        + E2
        * (
            d1_pow_h1 * r1 * r2_pow_gamma12 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * gamma12 * log(r2)
            + d1_pow_h1
            * r1
            * r2_pow_gamma12
            * alpha12d2_pow_gamma12h2
            * r1C1h1_pow_gamma21
            * (gamma12 * h2)
            * logd2alpha12
            + d2_pow_h2 * r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * gamma12 * log(r2 * C2_pow_h2)
            + d2_pow_h2 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * gamma12 * log(r2)
            + d2_pow_h2
            * r2_pow_gamma12p1
            * alpha12d2_pow_gamma12h2
            * r1C1h1_pow_gamma21
            * (gamma12 * h2)
            * logd2alpha12
        )
        / (
            d1_pow_h1 * r1 * r2 * r1C1h1_pow_gamma21 * C2_pow_h2
            + d1_pow_h1 * r1 * r2 * r2C2h2_pow_gamma12 * C2_pow_h2
            + d1_pow_h1 * r1 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * C2_pow_h2
            + d1_pow_h1 * r1 * r2_pow_gamma12 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + d1_pow_h1 * r1_pow_gamma21p1 * r2_pow_gamma12 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
            + d1_pow_h1 * r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1
            + d2_pow_h2 * r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1
            + d2_pow_h2 * r1_pow_gamma21p1 * r2 * alpha21d1_pow_gamma21h1 * C1_pow_h1
            + d2_pow_h2 * r1_pow_gamma21 * r2 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1_pow_gamma21 * r2_pow_gamma12p1 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
            + d2_pow_h2 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * C2_pow_h2
            + r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * C2_pow_h2
            + r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * C1_pow_h1
            + r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * C2_pow_h2
        )
        + E3
        * (
            d2_pow_h2
            * r2
            * (r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            * (
                -(r2_pow_gamma12) * alpha12d2_pow_gamma12h2 * gamma12 * log(r2)
                - r2_pow_gamma12 * alpha12d2_pow_gamma12h2 * (gamma12 * h2) * logd2alpha12
            )
            * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r2 * C2_pow_h2)
            + d2_pow_h2
            * r2
            * (
                d1_pow_h1 * r1 * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r1 * C1_pow_h1)
                - (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r2 * C2_pow_h2)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
            * (
                r2_pow_gamma12 * alpha12d2_pow_gamma12h2 * gamma12 * log(r2)
                + r2_pow_gamma12 * alpha12d2_pow_gamma12h2 * (gamma12 * h2) * logd2alpha12
            )
            + (-d1_pow_h1 * r1 - d2_pow_h2 * r2)
            * (
                d1_pow_h1 * d2_pow_h2 * r1 * r2
                - (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
                * (d2_pow_h2 * r2 + r1_pow_gamma21 * alpha21d1_pow_gamma21h1 + r2 * C2_pow_h2)
            )
            * (
                r2_pow_gamma12 * alpha12d2_pow_gamma12h2 * gamma12 * log(r2)
                + r2_pow_gamma12 * alpha12d2_pow_gamma12h2 * (gamma12 * h2) * logd2alpha12
            )
            + (
                d1_pow_h1 * r1 * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r1 * C1_pow_h1)
                - (d1_pow_h1 * r1 + d2_pow_h2 * r2)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
            * (
                -(r2_pow_gamma12) * alpha12d2_pow_gamma12h2 * gamma12 * log(r2)
                - r2_pow_gamma12 * alpha12d2_pow_gamma12h2 * (gamma12 * h2) * logd2alpha12
            )
            * (d2_pow_h2 * r2 + r1_pow_gamma21 * alpha21d1_pow_gamma21h1 + r2 * C2_pow_h2)
        )
        / (
            -(
                (-d1_pow_h1 * r1 + r2C2h2_pow_gamma12) * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r1 * C1_pow_h1)
                + (d1_pow_h1 * r1 + d2_pow_h2 * r2)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
            * (
                d1_pow_h1 * d2_pow_h2 * r1 * r2
                - (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
                * (d2_pow_h2 * r2 + r1_pow_gamma21 * alpha21d1_pow_gamma21h1 + r2 * C2_pow_h2)
            )
            + (
                d1_pow_h1 * r1 * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r1 * C1_pow_h1)
                - (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r2 * C2_pow_h2)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
            * (
                -d2_pow_h2 * r2 * (d1_pow_h1 * r1 - r2C2h2_pow_gamma12)
                + (d2_pow_h2 * r2 - r1C1h1_pow_gamma21)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
        )
        + E3
        * (
            d2_pow_h2
            * r2
            * (r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            * (
                d1_pow_h1 * r1 * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r1 * C1_pow_h1)
                - (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r2 * C2_pow_h2)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
            + (
                d1_pow_h1 * r1 * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r1 * C1_pow_h1)
                - (d1_pow_h1 * r1 + d2_pow_h2 * r2)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
            * (
                d1_pow_h1 * d2_pow_h2 * r1 * r2
                - (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
                * (d2_pow_h2 * r2 + r1_pow_gamma21 * alpha21d1_pow_gamma21h1 + r2 * C2_pow_h2)
            )
        )
        * (
            -(
                -(-d1_pow_h1 * r1 + r2C2h2_pow_gamma12) * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r1 * C1_pow_h1)
                - (d1_pow_h1 * r1 + d2_pow_h2 * r2)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
            * (
                -(r2_pow_gamma12) * alpha12d2_pow_gamma12h2 * gamma12 * log(r2)
                - r2_pow_gamma12 * alpha12d2_pow_gamma12h2 * (gamma12 * h2) * logd2alpha12
            )
            * (d2_pow_h2 * r2 + r1_pow_gamma21 * alpha21d1_pow_gamma21h1 + r2 * C2_pow_h2)
            - (
                d1_pow_h1 * r1 * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r1 * C1_pow_h1)
                - (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r2 * C2_pow_h2)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
            * (
                d2_pow_h2 * r2 * r2C2h2_pow_gamma12 * gamma12 * log(r2 * C2_pow_h2)
                + (d2_pow_h2 * r2 - r1C1h1_pow_gamma21)
                * (
                    r2_pow_gamma12 * alpha12d2_pow_gamma12h2 * gamma12 * log(r2)
                    + r2_pow_gamma12 * alpha12d2_pow_gamma12h2 * (gamma12 * h2) * logd2alpha12
                )
            )
            - (
                -d2_pow_h2 * r2 * (d1_pow_h1 * r1 - r2C2h2_pow_gamma12)
                + (d2_pow_h2 * r2 - r1C1h1_pow_gamma21)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
            * (
                -(r2_pow_gamma12) * alpha12d2_pow_gamma12h2 * gamma12 * log(r2)
                - r2_pow_gamma12 * alpha12d2_pow_gamma12h2 * (gamma12 * h2) * logd2alpha12
            )
            * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r2 * C2_pow_h2)
            - (
                d1_pow_h1 * d2_pow_h2 * r1 * r2
                - (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
                * (d2_pow_h2 * r2 + r1_pow_gamma21 * alpha21d1_pow_gamma21h1 + r2 * C2_pow_h2)
            )
            * (
                -(r2C2h2_pow_gamma12)
                * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r1 * C1_pow_h1)
                * gamma12
                * log(r2 * C2_pow_h2)
                - (d1_pow_h1 * r1 + d2_pow_h2 * r2)
                * (
                    r2_pow_gamma12 * alpha12d2_pow_gamma12h2 * gamma12 * log(r2)
                    + r2_pow_gamma12 * alpha12d2_pow_gamma12h2 * (gamma12 * h2) * logd2alpha12
                )
            )
        )
        / (
            -(
                (-d1_pow_h1 * r1 + r2C2h2_pow_gamma12) * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r1 * C1_pow_h1)
                + (d1_pow_h1 * r1 + d2_pow_h2 * r2)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
            * (
                d1_pow_h1 * d2_pow_h2 * r1 * r2
                - (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
                * (d2_pow_h2 * r2 + r1_pow_gamma21 * alpha21d1_pow_gamma21h1 + r2 * C2_pow_h2)
            )
            + (
                d1_pow_h1 * r1 * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r1 * C1_pow_h1)
                - (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r2 * C2_pow_h2)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
            * (
                -d2_pow_h2 * r2 * (d1_pow_h1 * r1 - r2C2h2_pow_gamma12)
                + (d2_pow_h2 * r2 - r1C1h1_pow_gamma21)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
        )
        ** 2
    )

    # ********** loggamma21 ********

    j_loggamma21 = (
        E0
        * (
            r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * C2_pow_h2
            + r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * C2_pow_h2
            + r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * C1_pow_h1
            + r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * C2_pow_h2
        )
        * (
            -d1_pow_h1 * r1 * r2 * r1C1h1_pow_gamma21 * C2_pow_h2 * gamma21 * log(r1 * C1_pow_h1)
            - d1_pow_h1
            * r1
            * r2_pow_gamma12
            * alpha12d2_pow_gamma12h2
            * r1C1h1_pow_gamma21
            * gamma21
            * log(r1 * C1_pow_h1)
            - d1_pow_h1
            * r1_pow_gamma21p1
            * r2_pow_gamma12
            * alpha21d1_pow_gamma21h1
            * alpha12d2_pow_gamma12h2
            * gamma21
            * log(r1)
            - d1_pow_h1
            * r1_pow_gamma21p1
            * r2_pow_gamma12
            * alpha21d1_pow_gamma21h1
            * alpha12d2_pow_gamma12h2
            * (gamma21 * h1)
            * logd1alpha21
            - d1_pow_h1 * r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * gamma21 * log(r1)
            - d1_pow_h1
            * r1_pow_gamma21p1
            * alpha21d1_pow_gamma21h1
            * r2C2h2_pow_gamma12
            * (gamma21 * h1)
            * logd1alpha21
            - d2_pow_h2 * r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * gamma21 * log(r1 * C1_pow_h1)
            - d2_pow_h2 * r1_pow_gamma21p1 * r2 * alpha21d1_pow_gamma21h1 * C1_pow_h1 * gamma21 * log(r1)
            - d2_pow_h2 * r1_pow_gamma21p1 * r2 * alpha21d1_pow_gamma21h1 * C1_pow_h1 * (gamma21 * h1) * logd1alpha21
            - d2_pow_h2 * r1_pow_gamma21 * r2 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * gamma21 * log(r1)
            - d2_pow_h2
            * r1_pow_gamma21
            * r2
            * alpha21d1_pow_gamma21h1
            * r2C2h2_pow_gamma12
            * (gamma21 * h1)
            * logd1alpha21
            - d2_pow_h2
            * r1_pow_gamma21
            * r2_pow_gamma12p1
            * alpha21d1_pow_gamma21h1
            * alpha12d2_pow_gamma12h2
            * gamma21
            * log(r1)
            - d2_pow_h2
            * r1_pow_gamma21
            * r2_pow_gamma12p1
            * alpha21d1_pow_gamma21h1
            * alpha12d2_pow_gamma12h2
            * (gamma21 * h1)
            * logd1alpha21
            - d2_pow_h2
            * r2_pow_gamma12p1
            * alpha12d2_pow_gamma12h2
            * r1C1h1_pow_gamma21
            * gamma21
            * log(r1 * C1_pow_h1)
            - r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * C2_pow_h2 * gamma21 * log(r1 * C1_pow_h1)
            - r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * C1_pow_h1 * gamma21 * log(r1)
            - r1_pow_gamma21p1
            * alpha21d1_pow_gamma21h1
            * r2C2h2_pow_gamma12
            * C1_pow_h1
            * (gamma21 * h1)
            * logd1alpha21
            - r2_pow_gamma12p1
            * alpha12d2_pow_gamma12h2
            * r1C1h1_pow_gamma21
            * C2_pow_h2
            * gamma21
            * log(r1 * C1_pow_h1)
        )
        / (
            d1_pow_h1 * r1 * r2 * r1C1h1_pow_gamma21 * C2_pow_h2
            + d1_pow_h1 * r1 * r2 * r2C2h2_pow_gamma12 * C2_pow_h2
            + d1_pow_h1 * r1 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * C2_pow_h2
            + d1_pow_h1 * r1 * r2_pow_gamma12 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + d1_pow_h1 * r1_pow_gamma21p1 * r2_pow_gamma12 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
            + d1_pow_h1 * r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1
            + d2_pow_h2 * r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1
            + d2_pow_h2 * r1_pow_gamma21p1 * r2 * alpha21d1_pow_gamma21h1 * C1_pow_h1
            + d2_pow_h2 * r1_pow_gamma21 * r2 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1_pow_gamma21 * r2_pow_gamma12p1 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
            + d2_pow_h2 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * C2_pow_h2
            + r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * C2_pow_h2
            + r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * C1_pow_h1
            + r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * C2_pow_h2
        )
        ** 2
        + E0
        * (
            r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * C2_pow_h2 * gamma21 * log(r1 * C1_pow_h1)
            + r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * C1_pow_h1 * gamma21 * log(r1)
            + r1_pow_gamma21p1
            * alpha21d1_pow_gamma21h1
            * r2C2h2_pow_gamma12
            * C1_pow_h1
            * (gamma21 * h1)
            * logd1alpha21
            + r2_pow_gamma12p1
            * alpha12d2_pow_gamma12h2
            * r1C1h1_pow_gamma21
            * C2_pow_h2
            * gamma21
            * log(r1 * C1_pow_h1)
        )
        / (
            d1_pow_h1 * r1 * r2 * r1C1h1_pow_gamma21 * C2_pow_h2
            + d1_pow_h1 * r1 * r2 * r2C2h2_pow_gamma12 * C2_pow_h2
            + d1_pow_h1 * r1 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * C2_pow_h2
            + d1_pow_h1 * r1 * r2_pow_gamma12 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + d1_pow_h1 * r1_pow_gamma21p1 * r2_pow_gamma12 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
            + d1_pow_h1 * r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1
            + d2_pow_h2 * r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1
            + d2_pow_h2 * r1_pow_gamma21p1 * r2 * alpha21d1_pow_gamma21h1 * C1_pow_h1
            + d2_pow_h2 * r1_pow_gamma21 * r2 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1_pow_gamma21 * r2_pow_gamma12p1 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
            + d2_pow_h2 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * C2_pow_h2
            + r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * C2_pow_h2
            + r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * C1_pow_h1
            + r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * C2_pow_h2
        )
        + E1
        * (
            d1_pow_h1 * r1 * r2 * r1C1h1_pow_gamma21 * C2_pow_h2
            + d1_pow_h1 * r1 * r2 * r2C2h2_pow_gamma12 * C2_pow_h2
            + d1_pow_h1 * r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1_pow_gamma21 * r2 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
        )
        * (
            -d1_pow_h1 * r1 * r2 * r1C1h1_pow_gamma21 * C2_pow_h2 * gamma21 * log(r1 * C1_pow_h1)
            - d1_pow_h1
            * r1
            * r2_pow_gamma12
            * alpha12d2_pow_gamma12h2
            * r1C1h1_pow_gamma21
            * gamma21
            * log(r1 * C1_pow_h1)
            - d1_pow_h1
            * r1_pow_gamma21p1
            * r2_pow_gamma12
            * alpha21d1_pow_gamma21h1
            * alpha12d2_pow_gamma12h2
            * gamma21
            * log(r1)
            - d1_pow_h1
            * r1_pow_gamma21p1
            * r2_pow_gamma12
            * alpha21d1_pow_gamma21h1
            * alpha12d2_pow_gamma12h2
            * (gamma21 * h1)
            * logd1alpha21
            - d1_pow_h1 * r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * gamma21 * log(r1)
            - d1_pow_h1
            * r1_pow_gamma21p1
            * alpha21d1_pow_gamma21h1
            * r2C2h2_pow_gamma12
            * (gamma21 * h1)
            * logd1alpha21
            - d2_pow_h2 * r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * gamma21 * log(r1 * C1_pow_h1)
            - d2_pow_h2 * r1_pow_gamma21p1 * r2 * alpha21d1_pow_gamma21h1 * C1_pow_h1 * gamma21 * log(r1)
            - d2_pow_h2 * r1_pow_gamma21p1 * r2 * alpha21d1_pow_gamma21h1 * C1_pow_h1 * (gamma21 * h1) * logd1alpha21
            - d2_pow_h2 * r1_pow_gamma21 * r2 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * gamma21 * log(r1)
            - d2_pow_h2
            * r1_pow_gamma21
            * r2
            * alpha21d1_pow_gamma21h1
            * r2C2h2_pow_gamma12
            * (gamma21 * h1)
            * logd1alpha21
            - d2_pow_h2
            * r1_pow_gamma21
            * r2_pow_gamma12p1
            * alpha21d1_pow_gamma21h1
            * alpha12d2_pow_gamma12h2
            * gamma21
            * log(r1)
            - d2_pow_h2
            * r1_pow_gamma21
            * r2_pow_gamma12p1
            * alpha21d1_pow_gamma21h1
            * alpha12d2_pow_gamma12h2
            * (gamma21 * h1)
            * logd1alpha21
            - d2_pow_h2
            * r2_pow_gamma12p1
            * alpha12d2_pow_gamma12h2
            * r1C1h1_pow_gamma21
            * gamma21
            * log(r1 * C1_pow_h1)
            - r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * C2_pow_h2 * gamma21 * log(r1 * C1_pow_h1)
            - r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * C1_pow_h1 * gamma21 * log(r1)
            - r1_pow_gamma21p1
            * alpha21d1_pow_gamma21h1
            * r2C2h2_pow_gamma12
            * C1_pow_h1
            * (gamma21 * h1)
            * logd1alpha21
            - r2_pow_gamma12p1
            * alpha12d2_pow_gamma12h2
            * r1C1h1_pow_gamma21
            * C2_pow_h2
            * gamma21
            * log(r1 * C1_pow_h1)
        )
        / (
            d1_pow_h1 * r1 * r2 * r1C1h1_pow_gamma21 * C2_pow_h2
            + d1_pow_h1 * r1 * r2 * r2C2h2_pow_gamma12 * C2_pow_h2
            + d1_pow_h1 * r1 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * C2_pow_h2
            + d1_pow_h1 * r1 * r2_pow_gamma12 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + d1_pow_h1 * r1_pow_gamma21p1 * r2_pow_gamma12 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
            + d1_pow_h1 * r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1
            + d2_pow_h2 * r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1
            + d2_pow_h2 * r1_pow_gamma21p1 * r2 * alpha21d1_pow_gamma21h1 * C1_pow_h1
            + d2_pow_h2 * r1_pow_gamma21 * r2 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1_pow_gamma21 * r2_pow_gamma12p1 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
            + d2_pow_h2 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * C2_pow_h2
            + r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * C2_pow_h2
            + r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * C1_pow_h1
            + r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * C2_pow_h2
        )
        ** 2
        + E1
        * (
            d1_pow_h1 * r1 * r2 * r1C1h1_pow_gamma21 * C2_pow_h2 * gamma21 * log(r1 * C1_pow_h1)
            + d1_pow_h1 * r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * gamma21 * log(r1)
            + d1_pow_h1
            * r1_pow_gamma21p1
            * alpha21d1_pow_gamma21h1
            * r2C2h2_pow_gamma12
            * (gamma21 * h1)
            * logd1alpha21
            + d2_pow_h2 * r1_pow_gamma21 * r2 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * gamma21 * log(r1)
            + d2_pow_h2
            * r1_pow_gamma21
            * r2
            * alpha21d1_pow_gamma21h1
            * r2C2h2_pow_gamma12
            * (gamma21 * h1)
            * logd1alpha21
        )
        / (
            d1_pow_h1 * r1 * r2 * r1C1h1_pow_gamma21 * C2_pow_h2
            + d1_pow_h1 * r1 * r2 * r2C2h2_pow_gamma12 * C2_pow_h2
            + d1_pow_h1 * r1 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * C2_pow_h2
            + d1_pow_h1 * r1 * r2_pow_gamma12 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + d1_pow_h1 * r1_pow_gamma21p1 * r2_pow_gamma12 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
            + d1_pow_h1 * r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1
            + d2_pow_h2 * r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1
            + d2_pow_h2 * r1_pow_gamma21p1 * r2 * alpha21d1_pow_gamma21h1 * C1_pow_h1
            + d2_pow_h2 * r1_pow_gamma21 * r2 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1_pow_gamma21 * r2_pow_gamma12p1 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
            + d2_pow_h2 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * C2_pow_h2
            + r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * C2_pow_h2
            + r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * C1_pow_h1
            + r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * C2_pow_h2
        )
        + E2
        * (
            d1_pow_h1
            * r1
            * r2_pow_gamma12
            * alpha12d2_pow_gamma12h2
            * r1C1h1_pow_gamma21
            * gamma21
            * log(r1 * C1_pow_h1)
            + d2_pow_h2 * r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * gamma21 * log(r1 * C1_pow_h1)
            + d2_pow_h2
            * r2_pow_gamma12p1
            * alpha12d2_pow_gamma12h2
            * r1C1h1_pow_gamma21
            * gamma21
            * log(r1 * C1_pow_h1)
        )
        / (
            d1_pow_h1 * r1 * r2 * r1C1h1_pow_gamma21 * C2_pow_h2
            + d1_pow_h1 * r1 * r2 * r2C2h2_pow_gamma12 * C2_pow_h2
            + d1_pow_h1 * r1 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * C2_pow_h2
            + d1_pow_h1 * r1 * r2_pow_gamma12 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + d1_pow_h1 * r1_pow_gamma21p1 * r2_pow_gamma12 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
            + d1_pow_h1 * r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1
            + d2_pow_h2 * r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1
            + d2_pow_h2 * r1_pow_gamma21p1 * r2 * alpha21d1_pow_gamma21h1 * C1_pow_h1
            + d2_pow_h2 * r1_pow_gamma21 * r2 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1_pow_gamma21 * r2_pow_gamma12p1 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
            + d2_pow_h2 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * C2_pow_h2
            + r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * C2_pow_h2
            + r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * C1_pow_h1
            + r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * C2_pow_h2
        )
        + E2
        * (
            d1_pow_h1 * r1 * r2_pow_gamma12 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + d2_pow_h2 * r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1
            + d2_pow_h2 * r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1
            + d2_pow_h2 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
        )
        * (
            -d1_pow_h1 * r1 * r2 * r1C1h1_pow_gamma21 * C2_pow_h2 * gamma21 * log(r1 * C1_pow_h1)
            - d1_pow_h1
            * r1
            * r2_pow_gamma12
            * alpha12d2_pow_gamma12h2
            * r1C1h1_pow_gamma21
            * gamma21
            * log(r1 * C1_pow_h1)
            - d1_pow_h1
            * r1_pow_gamma21p1
            * r2_pow_gamma12
            * alpha21d1_pow_gamma21h1
            * alpha12d2_pow_gamma12h2
            * gamma21
            * log(r1)
            - d1_pow_h1
            * r1_pow_gamma21p1
            * r2_pow_gamma12
            * alpha21d1_pow_gamma21h1
            * alpha12d2_pow_gamma12h2
            * (gamma21 * h1)
            * logd1alpha21
            - d1_pow_h1 * r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * gamma21 * log(r1)
            - d1_pow_h1
            * r1_pow_gamma21p1
            * alpha21d1_pow_gamma21h1
            * r2C2h2_pow_gamma12
            * (gamma21 * h1)
            * logd1alpha21
            - d2_pow_h2 * r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * gamma21 * log(r1 * C1_pow_h1)
            - d2_pow_h2 * r1_pow_gamma21p1 * r2 * alpha21d1_pow_gamma21h1 * C1_pow_h1 * gamma21 * log(r1)
            - d2_pow_h2 * r1_pow_gamma21p1 * r2 * alpha21d1_pow_gamma21h1 * C1_pow_h1 * (gamma21 * h1) * logd1alpha21
            - d2_pow_h2 * r1_pow_gamma21 * r2 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * gamma21 * log(r1)
            - d2_pow_h2
            * r1_pow_gamma21
            * r2
            * alpha21d1_pow_gamma21h1
            * r2C2h2_pow_gamma12
            * (gamma21 * h1)
            * logd1alpha21
            - d2_pow_h2
            * r1_pow_gamma21
            * r2_pow_gamma12p1
            * alpha21d1_pow_gamma21h1
            * alpha12d2_pow_gamma12h2
            * gamma21
            * log(r1)
            - d2_pow_h2
            * r1_pow_gamma21
            * r2_pow_gamma12p1
            * alpha21d1_pow_gamma21h1
            * alpha12d2_pow_gamma12h2
            * (gamma21 * h1)
            * logd1alpha21
            - d2_pow_h2
            * r2_pow_gamma12p1
            * alpha12d2_pow_gamma12h2
            * r1C1h1_pow_gamma21
            * gamma21
            * log(r1 * C1_pow_h1)
            - r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * C2_pow_h2 * gamma21 * log(r1 * C1_pow_h1)
            - r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * C1_pow_h1 * gamma21 * log(r1)
            - r1_pow_gamma21p1
            * alpha21d1_pow_gamma21h1
            * r2C2h2_pow_gamma12
            * C1_pow_h1
            * (gamma21 * h1)
            * logd1alpha21
            - r2_pow_gamma12p1
            * alpha12d2_pow_gamma12h2
            * r1C1h1_pow_gamma21
            * C2_pow_h2
            * gamma21
            * log(r1 * C1_pow_h1)
        )
        / (
            d1_pow_h1 * r1 * r2 * r1C1h1_pow_gamma21 * C2_pow_h2
            + d1_pow_h1 * r1 * r2 * r2C2h2_pow_gamma12 * C2_pow_h2
            + d1_pow_h1 * r1 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * C2_pow_h2
            + d1_pow_h1 * r1 * r2_pow_gamma12 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + d1_pow_h1 * r1_pow_gamma21p1 * r2_pow_gamma12 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
            + d1_pow_h1 * r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1
            + d2_pow_h2 * r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1
            + d2_pow_h2 * r1_pow_gamma21p1 * r2 * alpha21d1_pow_gamma21h1 * C1_pow_h1
            + d2_pow_h2 * r1_pow_gamma21 * r2 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
            + d2_pow_h2 * r1_pow_gamma21 * r2_pow_gamma12p1 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
            + d2_pow_h2 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
            + r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * C2_pow_h2
            + r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * C2_pow_h2
            + r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * C1_pow_h1
            + r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * C2_pow_h2
        )
        ** 2
        + E3
        * (
            d1_pow_h1 * r1 * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r1 * C1_pow_h1)
            - (d1_pow_h1 * r1 + d2_pow_h2 * r2)
            * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
        )
        * (
            r1_pow_gamma21 * alpha21d1_pow_gamma21h1 * gamma21 * log(r1)
            + r1_pow_gamma21 * alpha21d1_pow_gamma21h1 * (gamma21 * h1) * logd1alpha21
        )
        * (-d1_pow_h1 * r1 - r1 * C1_pow_h1 - r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
        / (
            -(
                (-d1_pow_h1 * r1 + r2C2h2_pow_gamma12) * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r1 * C1_pow_h1)
                + (d1_pow_h1 * r1 + d2_pow_h2 * r2)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
            * (
                d1_pow_h1 * d2_pow_h2 * r1 * r2
                - (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
                * (d2_pow_h2 * r2 + r1_pow_gamma21 * alpha21d1_pow_gamma21h1 + r2 * C2_pow_h2)
            )
            + (
                d1_pow_h1 * r1 * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r1 * C1_pow_h1)
                - (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r2 * C2_pow_h2)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
            * (
                -d2_pow_h2 * r2 * (d1_pow_h1 * r1 - r2C2h2_pow_gamma12)
                + (d2_pow_h2 * r2 - r1C1h1_pow_gamma21)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
        )
        + E3
        * (
            d2_pow_h2
            * r2
            * (r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            * (
                d1_pow_h1 * r1 * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r1 * C1_pow_h1)
                - (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r2 * C2_pow_h2)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
            + (
                d1_pow_h1 * r1 * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r1 * C1_pow_h1)
                - (d1_pow_h1 * r1 + d2_pow_h2 * r2)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
            * (
                d1_pow_h1 * d2_pow_h2 * r1 * r2
                - (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
                * (d2_pow_h2 * r2 + r1_pow_gamma21 * alpha21d1_pow_gamma21h1 + r2 * C2_pow_h2)
            )
        )
        * (
            r1C1h1_pow_gamma21
            * (
                d1_pow_h1 * r1 * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r1 * C1_pow_h1)
                - (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r2 * C2_pow_h2)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
            * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            * gamma21
            * log(r1 * C1_pow_h1)
            - (
                -(-d1_pow_h1 * r1 + r2C2h2_pow_gamma12) * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r1 * C1_pow_h1)
                - (d1_pow_h1 * r1 + d2_pow_h2 * r2)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
            * (
                r1_pow_gamma21 * alpha21d1_pow_gamma21h1 * gamma21 * log(r1)
                + r1_pow_gamma21 * alpha21d1_pow_gamma21h1 * (gamma21 * h1) * logd1alpha21
            )
            * (-d1_pow_h1 * r1 - r1 * C1_pow_h1 - r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
        )
        / (
            -(
                (-d1_pow_h1 * r1 + r2C2h2_pow_gamma12) * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r1 * C1_pow_h1)
                + (d1_pow_h1 * r1 + d2_pow_h2 * r2)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
            * (
                d1_pow_h1 * d2_pow_h2 * r1 * r2
                - (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
                * (d2_pow_h2 * r2 + r1_pow_gamma21 * alpha21d1_pow_gamma21h1 + r2 * C2_pow_h2)
            )
            + (
                d1_pow_h1 * r1 * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r1 * C1_pow_h1)
                - (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r2 * C2_pow_h2)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
            * (
                -d2_pow_h2 * r2 * (d1_pow_h1 * r1 - r2C2h2_pow_gamma12)
                + (d2_pow_h2 * r2 - r1C1h1_pow_gamma21)
                * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            )
        )
        ** 2
    )

    # ********** E0 ********

    j_E0 = (
        r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * C2_pow_h2
        + r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * C2_pow_h2
        + r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * C1_pow_h1
        + r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * C2_pow_h2
    ) / (
        d1_pow_h1 * r1 * r2 * r1C1h1_pow_gamma21 * C2_pow_h2
        + d1_pow_h1 * r1 * r2 * r2C2h2_pow_gamma12 * C2_pow_h2
        + d1_pow_h1 * r1 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * C2_pow_h2
        + d1_pow_h1 * r1 * r2_pow_gamma12 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
        + d1_pow_h1 * r1_pow_gamma21p1 * r2_pow_gamma12 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
        + d1_pow_h1 * r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
        + d2_pow_h2 * r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1
        + d2_pow_h2 * r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1
        + d2_pow_h2 * r1_pow_gamma21p1 * r2 * alpha21d1_pow_gamma21h1 * C1_pow_h1
        + d2_pow_h2 * r1_pow_gamma21 * r2 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
        + d2_pow_h2 * r1_pow_gamma21 * r2_pow_gamma12p1 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
        + d2_pow_h2 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
        + r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * C2_pow_h2
        + r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * C2_pow_h2
        + r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * C1_pow_h1
        + r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * C2_pow_h2
    )

    # ********** E1 ********

    j_E1 = (
        d1_pow_h1 * r1 * r2 * r1C1h1_pow_gamma21 * C2_pow_h2
        + d1_pow_h1 * r1 * r2 * r2C2h2_pow_gamma12 * C2_pow_h2
        + d1_pow_h1 * r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
        + d2_pow_h2 * r1_pow_gamma21 * r2 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
    ) / (
        d1_pow_h1 * r1 * r2 * r1C1h1_pow_gamma21 * C2_pow_h2
        + d1_pow_h1 * r1 * r2 * r2C2h2_pow_gamma12 * C2_pow_h2
        + d1_pow_h1 * r1 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * C2_pow_h2
        + d1_pow_h1 * r1 * r2_pow_gamma12 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
        + d1_pow_h1 * r1_pow_gamma21p1 * r2_pow_gamma12 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
        + d1_pow_h1 * r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
        + d2_pow_h2 * r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1
        + d2_pow_h2 * r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1
        + d2_pow_h2 * r1_pow_gamma21p1 * r2 * alpha21d1_pow_gamma21h1 * C1_pow_h1
        + d2_pow_h2 * r1_pow_gamma21 * r2 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
        + d2_pow_h2 * r1_pow_gamma21 * r2_pow_gamma12p1 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
        + d2_pow_h2 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
        + r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * C2_pow_h2
        + r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * C2_pow_h2
        + r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * C1_pow_h1
        + r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * C2_pow_h2
    )

    # ********** E2 ********

    j_E2 = (
        d1_pow_h1 * r1 * r2_pow_gamma12 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
        + d2_pow_h2 * r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1
        + d2_pow_h2 * r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1
        + d2_pow_h2 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
    ) / (
        d1_pow_h1 * r1 * r2 * r1C1h1_pow_gamma21 * C2_pow_h2
        + d1_pow_h1 * r1 * r2 * r2C2h2_pow_gamma12 * C2_pow_h2
        + d1_pow_h1 * r1 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * C2_pow_h2
        + d1_pow_h1 * r1 * r2_pow_gamma12 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
        + d1_pow_h1 * r1_pow_gamma21p1 * r2_pow_gamma12 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
        + d1_pow_h1 * r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
        + d2_pow_h2 * r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1
        + d2_pow_h2 * r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1
        + d2_pow_h2 * r1_pow_gamma21p1 * r2 * alpha21d1_pow_gamma21h1 * C1_pow_h1
        + d2_pow_h2 * r1_pow_gamma21 * r2 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12
        + d2_pow_h2 * r1_pow_gamma21 * r2_pow_gamma12p1 * alpha21d1_pow_gamma21h1 * alpha12d2_pow_gamma12h2
        + d2_pow_h2 * r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21
        + r1 * r2 * r1C1h1_pow_gamma21 * C1_pow_h1 * C2_pow_h2
        + r1 * r2 * r2C2h2_pow_gamma12 * C1_pow_h1 * C2_pow_h2
        + r1_pow_gamma21p1 * alpha21d1_pow_gamma21h1 * r2C2h2_pow_gamma12 * C1_pow_h1
        + r2_pow_gamma12p1 * alpha12d2_pow_gamma12h2 * r1C1h1_pow_gamma21 * C2_pow_h2
    )

    # ********** E3 ********

    j_E3 = (
        d2_pow_h2
        * r2
        * (r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
        * (
            d1_pow_h1 * r1 * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r1 * C1_pow_h1)
            - (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r2 * C2_pow_h2)
            * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
        )
        + (
            d1_pow_h1 * r1 * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r1 * C1_pow_h1)
            - (d1_pow_h1 * r1 + d2_pow_h2 * r2)
            * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
        )
        * (
            d1_pow_h1 * d2_pow_h2 * r1 * r2
            - (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            * (d2_pow_h2 * r2 + r1_pow_gamma21 * alpha21d1_pow_gamma21h1 + r2 * C2_pow_h2)
        )
    ) / (
        -(
            (-d1_pow_h1 * r1 + r2C2h2_pow_gamma12) * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r1 * C1_pow_h1)
            + (d1_pow_h1 * r1 + d2_pow_h2 * r2)
            * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
        )
        * (
            d1_pow_h1 * d2_pow_h2 * r1 * r2
            - (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
            * (d2_pow_h2 * r2 + r1_pow_gamma21 * alpha21d1_pow_gamma21h1 + r2 * C2_pow_h2)
        )
        + (
            d1_pow_h1 * r1 * (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r1 * C1_pow_h1)
            - (d1_pow_h1 * r1 + d2_pow_h2 * r2 + r2 * C2_pow_h2)
            * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
        )
        * (
            -d2_pow_h2 * r2 * (d1_pow_h1 * r1 - r2C2h2_pow_gamma12)
            + (d2_pow_h2 * r2 - r1C1h1_pow_gamma21)
            * (d1_pow_h1 * r1 + r1 * C1_pow_h1 + r2_pow_gamma12 * alpha12d2_pow_gamma12h2)
        )
    )

    # E0, E1, E2, E3, logh1, logh2, logC1, logC2, logalpha12, logalpha21
    jac = np.hstack(
        [
            j.reshape(-1, 1)
            for j in [
                j_E0,
                j_E1,
                j_E2,
                j_E3,
                j_logh1,
                j_logh2,
                j_logC1,
                j_logC2,
                j_logalpha12,
                j_logalpha21,
                j_loggamma12,
                j_loggamma21,
            ]
        ]
    )
    jac[np.isnan(jac)] = 0
    return jac
