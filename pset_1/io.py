from contextlib import contextmanager
import os, tempfile

@contextmanager
def atomic_write(file, mode="w", as_file=True, suffix='.bak', prefix='tmp', text=True):
    """Write a file atomically

    :param file: str or :class:`os.PathLike` target to write

    :param bool as_file:  if True, the yielded object is a :class:File.
        (eg, what you get with `open(...)`).  Otherwise, it will be the
        temporary file path string

    :param kwargs: anything else needed to open the file

    :raises: FileExistsError if target exists

    Example::

        with atomic_write("hello.txt") as f:
            f.write("world!")

    """

    if os.path.isfile(file):
        raise Exception(FileExistsError)
    path = os.path.dirname(file)
    fd, tmp = tempfile.mkstemp(suffix='.bak', prefix='tmp', dir=path, text=text)
    try:
        if as_file != True:
            print(tmp)
        else:
            with os.fdopen(fd, 'w' if mode == 'w' else 'wb') as f:
                yield f
            os.rename(tmp, file)
            tmp = None


    finally:
        if tmp is not None:
            try:
                os.unlink(tmp)
            except OSError:
                pass

# with atomic_write("hello.txt", as_file= False) as w:
#     w.write('world!')