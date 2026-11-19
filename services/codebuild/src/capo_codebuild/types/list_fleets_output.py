"""Generated from Smithy shape ``com.amazonaws.codebuild#ListFleetsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.fleet_arns
    import capo_codebuild.types.string


class ListFleetsOutput(TypedDict, closed=True):
    next_token: NotRequired["capo_codebuild.types.string.String"]
    """<p>If there are more than 100 items in the list, only the first 100 items are returned, along with a unique string called a <i>nextToken</i>. To get the next batch of items in the list, call this operation again, adding the next token to the call.</p>"""
    fleets: NotRequired["capo_codebuild.types.fleet_arns.FleetArns"]
    """<p>The list of compute fleet names.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListFleetsOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "fleets" in value:
        import capo_codebuild.types.fleet_arns

        out["fleets"] = capo_codebuild.types.fleet_arns.serialize_aws_json_1_1(
            value["fleets"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListFleetsOutput:
    out: ListFleetsOutput = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("fleets") is not None:
        import capo_codebuild.types.fleet_arns

        out["fleets"] = capo_codebuild.types.fleet_arns.deserialize_aws_json_1_1(
            data["fleets"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListFleetsOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "fleets" in value:
        import capo_codebuild.types.fleet_arns

        out["fleets"] = capo_codebuild.types.fleet_arns.serialize_cbor(value["fleets"])
    return out


def deserialize_cbor(data: dict) -> ListFleetsOutput:
    out: ListFleetsOutput = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("fleets") is not None:
        import capo_codebuild.types.fleet_arns

        out["fleets"] = capo_codebuild.types.fleet_arns.deserialize_cbor(data["fleets"])
    return out
