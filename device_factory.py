# import json

from supported_devices.power_plugs import Mss310, Mss425e


def build_wrapper(
        token,
        key,
        user_id,
        device_type,  # type: str
        device_specs  # type: dict
):
    if device_type.lower() == "mss310":
        # print(device_type)
        # print(json.dumps(device_specs, indent=4))
        return Mss310(token, key, user_id, **device_specs)
    elif device_type.lower() == "mss425e":
        # print(device_type)
        # print(json.dumps(device_specs, indent=4))
        return Mss425e(token, key, user_id, **device_specs)
    else:
        print(device_type.lower())
        return None
