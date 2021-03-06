# automatically generated by the FlatBuffers compiler, do not modify

# namespace: ppx

import flatbuffers

class Sample(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsSample(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Sample()
        x.Init(buf, n + offset)
        return x

    # Sample
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Sample
    def Address(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # Sample
    def Name(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # Sample
    def DistributionType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

    # Sample
    def Distribution(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            from flatbuffers.table import Table
            obj = Table(bytearray(), 0)
            self._tab.Union(obj, o)
            return obj
        return None

    # Sample
    def Control(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return True

    # Sample
    def Replace(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

def SampleStart(builder): builder.StartObject(6)
def SampleAddAddress(builder, address): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(address), 0)
def SampleAddName(builder, name): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(name), 0)
def SampleAddDistributionType(builder, distributionType): builder.PrependUint8Slot(2, distributionType, 0)
def SampleAddDistribution(builder, distribution): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(distribution), 0)
def SampleAddControl(builder, control): builder.PrependBoolSlot(4, control, 1)
def SampleAddReplace(builder, replace): builder.PrependBoolSlot(5, replace, 0)
def SampleEnd(builder): return builder.EndObject()
