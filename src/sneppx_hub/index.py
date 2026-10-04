"""In-memory index of signed models mirrored from sneppx-forge."""


class ModelIndex:
    def __init__(self):
        self._models = {}

    def add(self, name, uri, version="1.0.0", tags=None, signed=True):
        if not name or not uri:
            raise ValueError("name and uri required")
        entry = {"name": name, "uri": uri, "version": version, "tags": list(tags or []), "signed": signed}
        self._models[name] = entry
        return entry

    def get(self, name):
        return self._models.get(name)

    def search(self, tag=None, signed_only=False):
        out = []
        for m in self._models.values():
            if tag is not None and tag not in m["tags"]:
                continue
            if signed_only and not m["signed"]:
                continue
            out.append(m)
        return out

    def list(self):
        return list(self._models.values())
