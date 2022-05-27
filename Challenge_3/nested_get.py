def nested_get(input_dict, nested_key):
    internal_dict_value = input_dict
    for k in nested_key:
        internal_dict_value = internal_dict_value.get(k, None)
        if internal_dict_value is None:
            return None
    return internal_dict_value

print(nested_get({"a":{"b":{"c":"a"}}},["a","b","c"]))
print(nested_get({"a":{"dog":{60,70,80}}},["a","cat"])) 
print(nested_get({"cat":{"dog":{60,70,80}}},["cat","dog"])) 