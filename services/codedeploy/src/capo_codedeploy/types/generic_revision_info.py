"""Generated from Smithy shape ``com.amazonaws.codedeploy#GenericRevisionInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.deployment_groups_list
    import capo_codedeploy.types.description
    import capo_codedeploy.types.timestamp


class GenericRevisionInfo(TypedDict, closed=True):
    description: NotRequired["capo_codedeploy.types.description.Description"]
    """<p>A comment about the revision.</p>"""
    deployment_groups: NotRequired[
        "capo_codedeploy.types.deployment_groups_list.DeploymentGroupsList"
    ]
    """<p>The deployment groups for which this is the current target revision.</p>"""
    first_used_time: NotRequired["capo_codedeploy.types.timestamp.Timestamp"]
    """<p>When the revision was first used by CodeDeploy.</p>"""
    last_used_time: NotRequired["capo_codedeploy.types.timestamp.Timestamp"]
    """<p>When the revision was last used by CodeDeploy.</p>"""
    register_time: NotRequired["capo_codedeploy.types.timestamp.Timestamp"]
    """<p>When the revision was registered with CodeDeploy.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GenericRevisionInfo) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    if "deployment_groups" in value:
        import capo_codedeploy.types.deployment_groups_list

        out["deploymentGroups"] = (
            capo_codedeploy.types.deployment_groups_list.serialize_aws_json_1_1(
                value["deployment_groups"]
            )
        )
    if "first_used_time" in value:
        import capo_codedeploy.types.timestamp

        out["firstUsedTime"] = capo_codedeploy.types.timestamp.serialize_aws_json_1_1(
            value["first_used_time"]
        )
    if "last_used_time" in value:
        import capo_codedeploy.types.timestamp

        out["lastUsedTime"] = capo_codedeploy.types.timestamp.serialize_aws_json_1_1(
            value["last_used_time"]
        )
    if "register_time" in value:
        import capo_codedeploy.types.timestamp

        out["registerTime"] = capo_codedeploy.types.timestamp.serialize_aws_json_1_1(
            value["register_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GenericRevisionInfo:
    out: GenericRevisionInfo = {}  # type: ignore[typeddict-item]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("deploymentGroups") is not None:
        import capo_codedeploy.types.deployment_groups_list

        out["deployment_groups"] = (
            capo_codedeploy.types.deployment_groups_list.deserialize_aws_json_1_1(
                data["deploymentGroups"]
            )
        )
    if data.get("firstUsedTime") is not None:
        import capo_codedeploy.types.timestamp

        out["first_used_time"] = (
            capo_codedeploy.types.timestamp.deserialize_aws_json_1_1(
                data["firstUsedTime"]
            )
        )
    if data.get("lastUsedTime") is not None:
        import capo_codedeploy.types.timestamp

        out["last_used_time"] = (
            capo_codedeploy.types.timestamp.deserialize_aws_json_1_1(
                data["lastUsedTime"]
            )
        )
    if data.get("registerTime") is not None:
        import capo_codedeploy.types.timestamp

        out["register_time"] = capo_codedeploy.types.timestamp.deserialize_aws_json_1_1(
            data["registerTime"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GenericRevisionInfo) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    if "deployment_groups" in value:
        import capo_codedeploy.types.deployment_groups_list

        out["deploymentGroups"] = (
            capo_codedeploy.types.deployment_groups_list.serialize_cbor(
                value["deployment_groups"]
            )
        )
    if "first_used_time" in value:
        import capo_codedeploy.types.timestamp

        out["firstUsedTime"] = capo_codedeploy.types.timestamp.serialize_cbor(
            value["first_used_time"]
        )
    if "last_used_time" in value:
        import capo_codedeploy.types.timestamp

        out["lastUsedTime"] = capo_codedeploy.types.timestamp.serialize_cbor(
            value["last_used_time"]
        )
    if "register_time" in value:
        import capo_codedeploy.types.timestamp

        out["registerTime"] = capo_codedeploy.types.timestamp.serialize_cbor(
            value["register_time"]
        )
    return out


def deserialize_cbor(data: dict) -> GenericRevisionInfo:
    out: GenericRevisionInfo = {}  # type: ignore[typeddict-item]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("deploymentGroups") is not None:
        import capo_codedeploy.types.deployment_groups_list

        out["deployment_groups"] = (
            capo_codedeploy.types.deployment_groups_list.deserialize_cbor(
                data["deploymentGroups"]
            )
        )
    if data.get("firstUsedTime") is not None:
        import capo_codedeploy.types.timestamp

        out["first_used_time"] = capo_codedeploy.types.timestamp.deserialize_cbor(
            data["firstUsedTime"]
        )
    if data.get("lastUsedTime") is not None:
        import capo_codedeploy.types.timestamp

        out["last_used_time"] = capo_codedeploy.types.timestamp.deserialize_cbor(
            data["lastUsedTime"]
        )
    if data.get("registerTime") is not None:
        import capo_codedeploy.types.timestamp

        out["register_time"] = capo_codedeploy.types.timestamp.deserialize_cbor(
            data["registerTime"]
        )
    return out
