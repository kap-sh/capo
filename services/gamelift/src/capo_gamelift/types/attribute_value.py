"""Generated from Smithy shape ``com.amazonaws.gamelift#AttributeValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.double_object
    import capo_gamelift.types.player_attribute_string
    import capo_gamelift.types.player_attribute_string_double_map
    import capo_gamelift.types.player_attribute_string_list


class AttributeValue(TypedDict, closed=True):
    s: NotRequired["capo_gamelift.types.player_attribute_string.PlayerAttributeString"]
    """<p>For single string values. Maximum string length is 100 characters.</p>"""
    n: NotRequired["capo_gamelift.types.double_object.DoubleObject"]
    """<p>For number values, expressed as double.</p>"""
    sl: NotRequired[
        "capo_gamelift.types.player_attribute_string_list.PlayerAttributeStringList"
    ]
    """<p>For a list of up to 100 strings. Maximum length for each string is 100 characters. Duplicate values are not recognized; all occurrences of the repeated value after the first of a repeated value are ignored.</p>"""
    sdm: NotRequired[
        "capo_gamelift.types.player_attribute_string_double_map.PlayerAttributeStringDoubleMap"
    ]
    """<p>For a map of up to 10 data type:value pairs. Maximum length for each string value is 100 characters. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AttributeValue) -> dict:
    out: dict = {}
    if "s" in value:
        out["S"] = value["s"]
    if "n" in value:
        out["N"] = (
            "NaN"
            if value["n"] != value["n"]
            else "Infinity"
            if value["n"] == float("inf")
            else "-Infinity"
            if value["n"] == float("-inf")
            else value["n"]
        )
    if "sl" in value:
        import capo_gamelift.types.player_attribute_string_list

        out["SL"] = (
            capo_gamelift.types.player_attribute_string_list.serialize_aws_json_1_1(
                value["sl"]
            )
        )
    if "sdm" in value:
        import capo_gamelift.types.player_attribute_string_double_map

        out["SDM"] = (
            capo_gamelift.types.player_attribute_string_double_map.serialize_aws_json_1_1(
                value["sdm"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AttributeValue:
    out: AttributeValue = {}  # type: ignore[typeddict-item]
    if data.get("S") is not None:
        out["s"] = data["S"]
    if data.get("N") is not None:
        out["n"] = float(data["N"])
    if data.get("SL") is not None:
        import capo_gamelift.types.player_attribute_string_list

        out["sl"] = (
            capo_gamelift.types.player_attribute_string_list.deserialize_aws_json_1_1(
                data["SL"]
            )
        )
    if data.get("SDM") is not None:
        import capo_gamelift.types.player_attribute_string_double_map

        out["sdm"] = (
            capo_gamelift.types.player_attribute_string_double_map.deserialize_aws_json_1_1(
                data["SDM"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AttributeValue) -> dict:
    out: dict = {}
    if "s" in value:
        out["S"] = value["s"]
    if "n" in value:
        out["N"] = value["n"]
    if "sl" in value:
        import capo_gamelift.types.player_attribute_string_list

        out["SL"] = capo_gamelift.types.player_attribute_string_list.serialize_cbor(
            value["sl"]
        )
    if "sdm" in value:
        import capo_gamelift.types.player_attribute_string_double_map

        out["SDM"] = (
            capo_gamelift.types.player_attribute_string_double_map.serialize_cbor(
                value["sdm"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> AttributeValue:
    out: AttributeValue = {}  # type: ignore[typeddict-item]
    if data.get("S") is not None:
        out["s"] = data["S"]
    if data.get("N") is not None:
        out["n"] = float(data["N"])
    if data.get("SL") is not None:
        import capo_gamelift.types.player_attribute_string_list

        out["sl"] = capo_gamelift.types.player_attribute_string_list.deserialize_cbor(
            data["SL"]
        )
    if data.get("SDM") is not None:
        import capo_gamelift.types.player_attribute_string_double_map

        out["sdm"] = (
            capo_gamelift.types.player_attribute_string_double_map.deserialize_cbor(
                data["SDM"]
            )
        )
    return out
