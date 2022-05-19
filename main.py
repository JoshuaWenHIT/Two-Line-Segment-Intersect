# Previous Version
def __intersect_pre(point_aa, point_bb,
                point_cc, point_dd):
    # this fuction will judge whether two line-segment is intersect
    # from https://stackoverflow.com/questions/563198/how-do-you-detect-where-two-line-segments-intersect
    s10_x = point_bb[0] - point_aa[0]
    s10_y = point_bb[1] - point_aa[1]
    s32_x = point_dd[0] - point_cc[0]
    s32_y = point_dd[1] - point_cc[1]

    denom = s10_x * s32_y - s32_x * s10_y
    if denom == 0:
        return False

    denomPositive = denom > 0

    s02_x = point_aa[0] - point_cc[0]
    s02_y = point_aa[1] - point_cc[1]
    s_numer = s10_x * s02_y - s10_y * s02_x
    if (s_numer < 0) == denomPositive:
        return False
    t_numer = s32_x * s02_y - s32_y * s02_x
    if (t_numer < 0) == denomPositive:
        return False

    if ((s_numer > denom) == denomPositive) or ((t_numer > denom) == denomPositive):
        return False

    return True


# New Version by Joshua Wen
def __intersect(point_aa, point_bb,
                point_cc, point_dd):
    # this fuction will judge whether two line-segment is intersect
    # from https://github.com/JoshuaWenHIT/Two-Line-Segment-Intersect
    s10_x = point_bb[0] - point_aa[0]
    s10_y = point_bb[1] - point_aa[1]
    s32_x = point_dd[0] - point_cc[0]
    s32_y = point_dd[1] - point_cc[1]
    s20_x = point_cc[0] - point_aa[0]
    s20_y = point_cc[1] - point_aa[1]

    denom = s10_x * s32_y - s32_x * s10_y
    denomPositive = denom > 0

    if denom == 0:
        if (s20_x * s10_y - s20_y * s10_x) == 0:
            m = (s20_x * s32_x + s20_y * s32_y) / (s32_x ^ 2 + s32_y ^ 2)
            n = (s20_x * s10_x + s20_y * s10_y) / (s10_x ^ 2 + s10_y ^ 2)
            if 0 <= m <= 1 and 0 <= n <= 1:
                return True
            else:
                return False
        else:
            return False

    denom_diff = s20_x * s10_y - s20_y * s10_x
    if (denom_diff <= 0) == denomPositive:
        return False

    denom_diff_ = s20_x * s32_y - s20_y * s32_x
    if (denom_diff_ <= 0) == denomPositive:
        return False

    if ((denom_diff > denom) == denomPositive) or ((denom_diff_ > denom) == denomPositive):
        return False

    return True
