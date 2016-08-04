
class SepText:

  def __init__(self, sep, text=None, file=None):
    self._sep = sep
    # if text != None:
    #   self._data = self.
      # open(fname, mode)

  # def __del__(self):
  #   self._file.close()

  def _pars_text(self, text):
    lines = text.splitlines()
    return self._pars_lines(lines)

  def _pars_lines(self, lines):

    data = []


  def get_strlst(self):
    return self._file.readlines()

  def get_array(self, sep=None):
    return [str.split(sep) for str in self.get_strlst()]

  def get_dict(self, sep=None):
    arr = self.get_array(sep)
    titles = arr[0]
    dict = []
    for rec in arr[1:]:
      dict.append({titles[fnum]: fval for fnum, fval in enumerate(rec, 0)})
        #~ print titles[fnum], ": ", fval
        #~ raw_input()
        #~ dict.append({titles[fnum]: fval})
    return dict