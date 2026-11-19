"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#IdleDimension``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer.types.idle_dimension_key
    import capo_compute_optimizer.types.idle_dimension_values


class IdleDimension(TypedDict, closed=True):
    key: NotRequired["capo_compute_optimizer.types.idle_dimension_key.IdleDimensionKey"]
    """<p>The name of the dimension key.</p>"""
    values: NotRequired[
        "capo_compute_optimizer.types.idle_dimension_values.IdleDimensionValues"
    ]
    """<p>The value of the dimension.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IdleDimension) -> dict:
    out: dict = {}
    if "key" in value:
        out["key"] = value["key"]
    if "values" in value:
        import capo_compute_optimizer.types.idle_dimension_values

        out["values"] = (
            capo_compute_optimizer.types.idle_dimension_values.serialize_aws_json_1_0(
                value["values"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> IdleDimension:
    out: IdleDimension = {}  # type: ignore[typeddict-item]
    if data.get("key") is not None:
        out["key"] = data["key"]
    if data.get("values") is not None:
        import capo_compute_optimizer.types.idle_dimension_values

        out["values"] = (
            capo_compute_optimizer.types.idle_dimension_values.deserialize_aws_json_1_0(
                data["values"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: IdleDimension) -> dict:
    out: dict = {}
    if "key" in value:
        out["key"] = value["key"]
    if "values" in value:
        import capo_compute_optimizer.types.idle_dimension_values

        out["values"] = (
            capo_compute_optimizer.types.idle_dimension_values.serialize_cbor(
                value["values"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> IdleDimension:
    out: IdleDimension = {}  # type: ignore[typeddict-item]
    if data.get("key") is not None:
        out["key"] = data["key"]
    if data.get("values") is not None:
        import capo_compute_optimizer.types.idle_dimension_values

        out["values"] = (
            capo_compute_optimizer.types.idle_dimension_values.deserialize_cbor(
                data["values"]
            )
        )
    return out
