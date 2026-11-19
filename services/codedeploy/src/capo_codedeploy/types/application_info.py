"""Generated from Smithy shape ``com.amazonaws.codedeploy#ApplicationInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.application_id
    import capo_codedeploy.types.application_name
    import capo_codedeploy.types.boolean
    import capo_codedeploy.types.compute_platform
    import capo_codedeploy.types.git_hub_account_token_name
    import capo_codedeploy.types.timestamp


class ApplicationInfo(TypedDict, closed=True):
    application_id: NotRequired["capo_codedeploy.types.application_id.ApplicationId"]
    """<p>The application ID.</p>"""
    application_name: NotRequired[
        "capo_codedeploy.types.application_name.ApplicationName"
    ]
    """<p>The application name.</p>"""
    create_time: NotRequired["capo_codedeploy.types.timestamp.Timestamp"]
    """<p>The time at which the application was created.</p>"""
    linked_to_git_hub: "capo_codedeploy.types.boolean.Boolean"
    """<p>True if the user has authenticated with GitHub for the specified application. Otherwise, false.</p>"""
    git_hub_account_name: NotRequired[
        "capo_codedeploy.types.git_hub_account_token_name.GitHubAccountTokenName"
    ]
    """<p>The name for a connection to a GitHub account.</p>"""
    compute_platform: NotRequired[
        "capo_codedeploy.types.compute_platform.ComputePlatform"
    ]
    """<p>The destination platform type for deployment of the application (<code>Lambda</code> or <code>Server</code>).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationInfo) -> dict:
    out: dict = {}
    if "application_id" in value:
        out["applicationId"] = value["application_id"]
    if "application_name" in value:
        out["applicationName"] = value["application_name"]
    if "create_time" in value:
        import capo_codedeploy.types.timestamp

        out["createTime"] = capo_codedeploy.types.timestamp.serialize_aws_json_1_1(
            value["create_time"]
        )
    out["linkedToGitHub"] = value.get("linked_to_git_hub", False)
    if "git_hub_account_name" in value:
        out["gitHubAccountName"] = value["git_hub_account_name"]
    if "compute_platform" in value:
        import capo_codedeploy.types.compute_platform

        out["computePlatform"] = (
            capo_codedeploy.types.compute_platform.serialize_aws_json_1_1(
                value["compute_platform"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ApplicationInfo:
    out: ApplicationInfo = {}  # type: ignore[typeddict-item]
    if data.get("applicationId") is not None:
        out["application_id"] = data["applicationId"]
    if data.get("applicationName") is not None:
        out["application_name"] = data["applicationName"]
    if data.get("createTime") is not None:
        import capo_codedeploy.types.timestamp

        out["create_time"] = capo_codedeploy.types.timestamp.deserialize_aws_json_1_1(
            data["createTime"]
        )
    if data.get("linkedToGitHub") is not None:
        out["linked_to_git_hub"] = data["linkedToGitHub"]
    else:
        out["linked_to_git_hub"] = False
    if data.get("gitHubAccountName") is not None:
        out["git_hub_account_name"] = data["gitHubAccountName"]
    if data.get("computePlatform") is not None:
        import capo_codedeploy.types.compute_platform

        out["compute_platform"] = (
            capo_codedeploy.types.compute_platform.deserialize_aws_json_1_1(
                data["computePlatform"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ApplicationInfo) -> dict:
    out: dict = {}
    if "application_id" in value:
        out["applicationId"] = value["application_id"]
    if "application_name" in value:
        out["applicationName"] = value["application_name"]
    if "create_time" in value:
        import capo_codedeploy.types.timestamp

        out["createTime"] = capo_codedeploy.types.timestamp.serialize_cbor(
            value["create_time"]
        )
    out["linkedToGitHub"] = value.get("linked_to_git_hub", False)
    if "git_hub_account_name" in value:
        out["gitHubAccountName"] = value["git_hub_account_name"]
    if "compute_platform" in value:
        import capo_codedeploy.types.compute_platform

        out["computePlatform"] = capo_codedeploy.types.compute_platform.serialize_cbor(
            value["compute_platform"]
        )
    return out


def deserialize_cbor(data: dict) -> ApplicationInfo:
    out: ApplicationInfo = {}  # type: ignore[typeddict-item]
    if data.get("applicationId") is not None:
        out["application_id"] = data["applicationId"]
    if data.get("applicationName") is not None:
        out["application_name"] = data["applicationName"]
    if data.get("createTime") is not None:
        import capo_codedeploy.types.timestamp

        out["create_time"] = capo_codedeploy.types.timestamp.deserialize_cbor(
            data["createTime"]
        )
    if data.get("linkedToGitHub") is not None:
        out["linked_to_git_hub"] = data["linkedToGitHub"]
    else:
        out["linked_to_git_hub"] = False
    if data.get("gitHubAccountName") is not None:
        out["git_hub_account_name"] = data["gitHubAccountName"]
    if data.get("computePlatform") is not None:
        import capo_codedeploy.types.compute_platform

        out["compute_platform"] = (
            capo_codedeploy.types.compute_platform.deserialize_cbor(
                data["computePlatform"]
            )
        )
    return out
