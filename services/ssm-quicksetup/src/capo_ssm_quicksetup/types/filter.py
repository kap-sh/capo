"""Generated from Smithy shape ``com.amazonaws.ssmquicksetup#Filter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ssm_quicksetup.types.filter_values


class Filter(TypedDict, closed=True):
    key: "str"
    """<p>The key for the filter.</p>"""
    values: "capo_ssm_quicksetup.types.filter_values.FilterValues"
    """<p>The values for the filter keys.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Filter) -> dict:
    out: dict = {}
    out["Key"] = value["key"]
    import capo_ssm_quicksetup.types.filter_values

    out["Values"] = capo_ssm_quicksetup.types.filter_values.serialize_json(
        value["values"]
    )
    return out


def deserialize_json(data: dict) -> Filter:
    out: Filter = {}  # type: ignore[typeddict-item]
    if data.get("Key") is not None:
        out["key"] = data["Key"]
    else:
        out["key"] = ""
    if data.get("Values") is not None:
        import capo_ssm_quicksetup.types.filter_values

        out["values"] = capo_ssm_quicksetup.types.filter_values.deserialize_json(
            data["Values"]
        )
    else:
        out["values"] = []
    return out
