"""Generated from Smithy shape ``com.amazonaws.codedeploy#ListDeploymentTargetsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.next_token
    import capo_codedeploy.types.target_id_list


class ListDeploymentTargetsOutput(TypedDict, closed=True):
    target_ids: NotRequired["capo_codedeploy.types.target_id_list.TargetIdList"]
    """<p> The unique IDs of deployment targets. </p>"""
    next_token: NotRequired["capo_codedeploy.types.next_token.NextToken"]
    """<p> If a large amount of information is returned, a token identifier is also returned. It can be used in a subsequent <code>ListDeploymentTargets</code> call to return the next set of deployment targets in the list. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDeploymentTargetsOutput) -> dict:
    out: dict = {}
    if "target_ids" in value:
        import capo_codedeploy.types.target_id_list

        out["targetIds"] = capo_codedeploy.types.target_id_list.serialize_aws_json_1_1(
            value["target_ids"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDeploymentTargetsOutput:
    out: ListDeploymentTargetsOutput = {}  # type: ignore[typeddict-item]
    if data.get("targetIds") is not None:
        import capo_codedeploy.types.target_id_list

        out["target_ids"] = (
            capo_codedeploy.types.target_id_list.deserialize_aws_json_1_1(
                data["targetIds"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListDeploymentTargetsOutput) -> dict:
    out: dict = {}
    if "target_ids" in value:
        import capo_codedeploy.types.target_id_list

        out["targetIds"] = capo_codedeploy.types.target_id_list.serialize_cbor(
            value["target_ids"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListDeploymentTargetsOutput:
    out: ListDeploymentTargetsOutput = {}  # type: ignore[typeddict-item]
    if data.get("targetIds") is not None:
        import capo_codedeploy.types.target_id_list

        out["target_ids"] = capo_codedeploy.types.target_id_list.deserialize_cbor(
            data["targetIds"]
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
