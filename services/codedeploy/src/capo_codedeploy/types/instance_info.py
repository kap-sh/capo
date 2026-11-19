"""Generated from Smithy shape ``com.amazonaws.codedeploy#InstanceInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.iam_session_arn
    import capo_codedeploy.types.iam_user_arn
    import capo_codedeploy.types.instance_arn
    import capo_codedeploy.types.instance_name
    import capo_codedeploy.types.tag_list
    import capo_codedeploy.types.timestamp


class InstanceInfo(TypedDict, closed=True):
    instance_name: NotRequired["capo_codedeploy.types.instance_name.InstanceName"]
    """<p>The name of the on-premises instance.</p>"""
    iam_session_arn: NotRequired["capo_codedeploy.types.iam_session_arn.IamSessionArn"]
    """<p>The ARN of the IAM session associated with the on-premises instance.</p>"""
    iam_user_arn: NotRequired["capo_codedeploy.types.iam_user_arn.IamUserArn"]
    """<p>The user ARN associated with the on-premises instance.</p>"""
    instance_arn: NotRequired["capo_codedeploy.types.instance_arn.InstanceArn"]
    """<p>The ARN of the on-premises instance.</p>"""
    register_time: NotRequired["capo_codedeploy.types.timestamp.Timestamp"]
    """<p>The time at which the on-premises instance was registered.</p>"""
    deregister_time: NotRequired["capo_codedeploy.types.timestamp.Timestamp"]
    """<p>If the on-premises instance was deregistered, the time at which the on-premises instance was deregistered.</p>"""
    tags: NotRequired["capo_codedeploy.types.tag_list.TagList"]
    """<p>The tags currently associated with the on-premises instance.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceInfo) -> dict:
    out: dict = {}
    if "instance_name" in value:
        out["instanceName"] = value["instance_name"]
    if "iam_session_arn" in value:
        out["iamSessionArn"] = value["iam_session_arn"]
    if "iam_user_arn" in value:
        out["iamUserArn"] = value["iam_user_arn"]
    if "instance_arn" in value:
        out["instanceArn"] = value["instance_arn"]
    if "register_time" in value:
        import capo_codedeploy.types.timestamp

        out["registerTime"] = capo_codedeploy.types.timestamp.serialize_aws_json_1_1(
            value["register_time"]
        )
    if "deregister_time" in value:
        import capo_codedeploy.types.timestamp

        out["deregisterTime"] = capo_codedeploy.types.timestamp.serialize_aws_json_1_1(
            value["deregister_time"]
        )
    if "tags" in value:
        import capo_codedeploy.types.tag_list

        out["tags"] = capo_codedeploy.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> InstanceInfo:
    out: InstanceInfo = {}  # type: ignore[typeddict-item]
    if data.get("instanceName") is not None:
        out["instance_name"] = data["instanceName"]
    if data.get("iamSessionArn") is not None:
        out["iam_session_arn"] = data["iamSessionArn"]
    if data.get("iamUserArn") is not None:
        out["iam_user_arn"] = data["iamUserArn"]
    if data.get("instanceArn") is not None:
        out["instance_arn"] = data["instanceArn"]
    if data.get("registerTime") is not None:
        import capo_codedeploy.types.timestamp

        out["register_time"] = capo_codedeploy.types.timestamp.deserialize_aws_json_1_1(
            data["registerTime"]
        )
    if data.get("deregisterTime") is not None:
        import capo_codedeploy.types.timestamp

        out["deregister_time"] = (
            capo_codedeploy.types.timestamp.deserialize_aws_json_1_1(
                data["deregisterTime"]
            )
        )
    if data.get("tags") is not None:
        import capo_codedeploy.types.tag_list

        out["tags"] = capo_codedeploy.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: InstanceInfo) -> dict:
    out: dict = {}
    if "instance_name" in value:
        out["instanceName"] = value["instance_name"]
    if "iam_session_arn" in value:
        out["iamSessionArn"] = value["iam_session_arn"]
    if "iam_user_arn" in value:
        out["iamUserArn"] = value["iam_user_arn"]
    if "instance_arn" in value:
        out["instanceArn"] = value["instance_arn"]
    if "register_time" in value:
        import capo_codedeploy.types.timestamp

        out["registerTime"] = capo_codedeploy.types.timestamp.serialize_cbor(
            value["register_time"]
        )
    if "deregister_time" in value:
        import capo_codedeploy.types.timestamp

        out["deregisterTime"] = capo_codedeploy.types.timestamp.serialize_cbor(
            value["deregister_time"]
        )
    if "tags" in value:
        import capo_codedeploy.types.tag_list

        out["tags"] = capo_codedeploy.types.tag_list.serialize_cbor(value["tags"])
    return out


def deserialize_cbor(data: dict) -> InstanceInfo:
    out: InstanceInfo = {}  # type: ignore[typeddict-item]
    if data.get("instanceName") is not None:
        out["instance_name"] = data["instanceName"]
    if data.get("iamSessionArn") is not None:
        out["iam_session_arn"] = data["iamSessionArn"]
    if data.get("iamUserArn") is not None:
        out["iam_user_arn"] = data["iamUserArn"]
    if data.get("instanceArn") is not None:
        out["instance_arn"] = data["instanceArn"]
    if data.get("registerTime") is not None:
        import capo_codedeploy.types.timestamp

        out["register_time"] = capo_codedeploy.types.timestamp.deserialize_cbor(
            data["registerTime"]
        )
    if data.get("deregisterTime") is not None:
        import capo_codedeploy.types.timestamp

        out["deregister_time"] = capo_codedeploy.types.timestamp.deserialize_cbor(
            data["deregisterTime"]
        )
    if data.get("tags") is not None:
        import capo_codedeploy.types.tag_list

        out["tags"] = capo_codedeploy.types.tag_list.deserialize_cbor(data["tags"])
    return out
