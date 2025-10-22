def sq_in_rect(lng, wdth):
    if lng == wdth:
        return None
    bigger = max(lng, wdth)
    smaller = min(lng, wdth)
    output = []
    while bigger != smaller:
        count = bigger // smaller
        output.extend([smaller] * count)
        bigger -= smaller
        bigger, smaller = smaller, bigger % smaller
        if smaller == 0:
            break
    return output

print(sq_in_rect(5,3))