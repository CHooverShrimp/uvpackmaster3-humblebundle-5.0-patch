from bpy.types import PropertyGroup

class StandalonePropertyGroupBase:

    @property
    def bl_rna(self):
        return self._pg_cls.bl_rna
    
    def cast_setattr(self, key, value):
        _types_func = {'BOOLEAN': bool, 'INT': int, 'FLOAT': float, 'STRING': str, 'ENUM': str}

        def _cast_value(_value, _type):
            _cast_func = _types_func.get(_type)
            if _cast_func is None:
                return _value
            return _cast_func(_value)

        prop_struct = self._pg_cls.bl_rna.properties.get(key, None)
        if prop_struct is not None and prop_struct.type in _types_func:
            prop_type = prop_struct.type
            is_array = getattr(prop_struct, 'is_array', False)
            if is_array:
                value = type(value)(_cast_value(v, prop_type) for v in value)
            else:
                value = _cast_value(value, prop_type)
        super().__setattr__(key, value)

    def property_unset(self, prop_name):
        prop_struct = self._pg_cls.bl_rna.properties[prop_name]
        is_array = getattr(prop_struct, 'is_array', False)
        if is_array and hasattr(prop_struct, 'default_array'):
            setattr(self, prop_name, prop_struct.default_array)
        elif hasattr(prop_struct, 'default'):
            setattr(self, prop_name, prop_struct.default)


def standalone_property_group(new_cls):
    pg_dict = dict()
    pg_exclude = { '__init__' }

    for id, value in new_cls.__dict__.items():
        if id not in pg_exclude:
            pg_dict[id] = value

    pg_cls = type(new_cls.__name__, (PropertyGroup,) + new_cls.__bases__, pg_dict)
    sa_cls = type(new_cls.__name__ + '_SA', (StandalonePropertyGroupBase,) + new_cls.__bases__, dict(new_cls.__dict__))
    pg_cls.SA = sa_cls
    sa_cls._pg_cls = pg_cls
    return pg_cls
