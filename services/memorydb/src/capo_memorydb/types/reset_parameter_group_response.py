"""Generated from Smithy shape ``com.amazonaws.memorydb#ResetParameterGroupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_memorydb.types.parameter_group


class ResetParameterGroupResponse(TypedDict, closed=True):
    parameter_group: NotRequired["capo_memorydb.types.parameter_group.ParameterGroup"]
    """<p>The parameter group being reset.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResetParameterGroupResponse) -> dict:
    out: dict = {}
    if "parameter_group" in value:
        import capo_memorydb.types.parameter_group

        out["ParameterGroup"] = (
            capo_memorydb.types.parameter_group.serialize_aws_json_1_1(
                value["parameter_group"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ResetParameterGroupResponse:
    out: ResetParameterGroupResponse = {}  # type: ignore[typeddict-item]
    if data.get("ParameterGroup") is not None:
        import capo_memorydb.types.parameter_group

        out["parameter_group"] = (
            capo_memorydb.types.parameter_group.deserialize_aws_json_1_1(
                data["ParameterGroup"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ResetParameterGroupResponse) -> dict:
    out: dict = {}
    if "parameter_group" in value:
        import capo_memorydb.types.parameter_group

        out["ParameterGroup"] = capo_memorydb.types.parameter_group.serialize_cbor(
            value["parameter_group"]
        )
    return out


def deserialize_cbor(data: dict) -> ResetParameterGroupResponse:
    out: ResetParameterGroupResponse = {}  # type: ignore[typeddict-item]
    if data.get("ParameterGroup") is not None:
        import capo_memorydb.types.parameter_group

        out["parameter_group"] = capo_memorydb.types.parameter_group.deserialize_cbor(
            data["ParameterGroup"]
        )
    return out
