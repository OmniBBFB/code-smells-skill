def affine_transform(x, y, *, m00, m01, m10, m11, tx, ty):
    """Independent, named coefficients of one affine transform."""
    return m00 * x + m01 * y + tx, m10 * x + m11 * y + ty

def sample():
    return affine_transform(1, 2, m00=1, m01=0, m10=0, m11=1, tx=2, ty=3)
