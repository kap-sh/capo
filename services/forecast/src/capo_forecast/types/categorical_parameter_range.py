"""Generated from Smithy shape ``com.amazonaws.forecast#CategoricalParameterRange``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_forecast.types.name
    import capo_forecast.types.values


class CategoricalParameterRange(TypedDict, closed=True):
    name: "capo_forecast.types.name.Name"
    """<p>The name of the categorical hyperparameter to tune.</p>"""
    values: "capo_forecast.types.values.Values"
    """<p>A list of the tunable categories for the hyperparameter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CategoricalParameterRange) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_forecast.types.values

    out["Values"] = capo_forecast.types.values.serialize_aws_json_1_1(value["values"])
    return out


def deserialize_aws_json_1_1(data: dict) -> CategoricalParameterRange:
    out: CategoricalParameterRange = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Values") is not None:
        import capo_forecast.types.values

        out["values"] = capo_forecast.types.values.deserialize_aws_json_1_1(
            data["Values"]
        )
    else:
        out["values"] = []
    return out
