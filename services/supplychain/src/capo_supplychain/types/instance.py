"""Generated from Smithy shape ``com.amazonaws.supplychain#Instance``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_supplychain.types.aws_account_id
    import capo_supplychain.types.instance_description
    import capo_supplychain.types.instance_name
    import capo_supplychain.types.instance_state
    import capo_supplychain.types.instance_web_app_dns_domain
    import capo_supplychain.types.kms_key_arn
    import capo_supplychain.types.uuid


class Instance(TypedDict, closed=True):
    instance_id: "capo_supplychain.types.uuid.UUID"
    """<p>The Amazon Web Services Supply Chain instance identifier.</p>"""
    aws_account_id: "capo_supplychain.types.aws_account_id.AwsAccountId"
    """<p>The Amazon Web Services account ID that owns the instance.</p>"""
    state: "capo_supplychain.types.instance_state.InstanceState"
    """<p>The state of the instance.</p>"""
    error_message: NotRequired["str"]
    """<p>The Amazon Web Services Supply Chain instance error message. If the instance results in an unhealthy state, customers need to check the error message, delete the current instance, and recreate a new one based on the mitigation from the error message.</p>"""
    web_app_dns_domain: NotRequired[
        "capo_supplychain.types.instance_web_app_dns_domain.InstanceWebAppDnsDomain"
    ]
    """<p>The WebApp DNS domain name of the instance.</p>"""
    created_time: NotRequired["datetime.datetime"]
    """<p>The instance creation timestamp.</p>"""
    last_modified_time: NotRequired["datetime.datetime"]
    """<p>The instance last modified timestamp.</p>"""
    instance_name: NotRequired["capo_supplychain.types.instance_name.InstanceName"]
    """<p>The Amazon Web Services Supply Chain instance name.</p>"""
    instance_description: NotRequired[
        "capo_supplychain.types.instance_description.InstanceDescription"
    ]
    """<p>The Amazon Web Services Supply Chain instance description.</p>"""
    kms_key_arn: NotRequired["capo_supplychain.types.kms_key_arn.KmsKeyArn"]
    """<p>The ARN (Amazon Resource Name) of the Key Management Service (KMS) key you optionally provided for encryption. If you did not provide anything here, AWS Supply Chain uses the Amazon Web Services owned KMS key and nothing is returned.</p>"""
    version_number: NotRequired["float"]
    """<p>The version number of the instance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Instance) -> dict:
    out: dict = {}
    out["instanceId"] = value["instance_id"]
    out["awsAccountId"] = value["aws_account_id"]
    import capo_supplychain.types.instance_state

    out["state"] = capo_supplychain.types.instance_state.serialize_json(value["state"])
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    if "web_app_dns_domain" in value:
        out["webAppDnsDomain"] = value["web_app_dns_domain"]
    if "created_time" in value:
        import capo_supplychain.types._prelude.timestamp

        out["createdTime"] = capo_supplychain.types._prelude.timestamp.serialize_json(
            value["created_time"]
        )
    if "last_modified_time" in value:
        import capo_supplychain.types._prelude.timestamp

        out["lastModifiedTime"] = (
            capo_supplychain.types._prelude.timestamp.serialize_json(
                value["last_modified_time"]
            )
        )
    if "instance_name" in value:
        out["instanceName"] = value["instance_name"]
    if "instance_description" in value:
        out["instanceDescription"] = value["instance_description"]
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    if "version_number" in value:
        out["versionNumber"] = (
            "NaN"
            if value["version_number"] != value["version_number"]
            else "Infinity"
            if value["version_number"] == float("inf")
            else "-Infinity"
            if value["version_number"] == float("-inf")
            else value["version_number"]
        )
    return out


def deserialize_json(data: dict) -> Instance:
    out: Instance = {}  # type: ignore[typeddict-item]
    if data.get("instanceId") is not None:
        out["instance_id"] = data["instanceId"]
    else:
        out["instance_id"] = ""
    if data.get("awsAccountId") is not None:
        out["aws_account_id"] = data["awsAccountId"]
    else:
        out["aws_account_id"] = ""
    if data.get("state") is not None:
        import capo_supplychain.types.instance_state

        out["state"] = capo_supplychain.types.instance_state.deserialize_json(
            data["state"]
        )
    else:
        import typing

        out["state"] = typing.cast(
            "capo_supplychain.types.instance_state.InstanceState", ""
        )
    if data.get("errorMessage") is not None:
        out["error_message"] = data["errorMessage"]
    if data.get("webAppDnsDomain") is not None:
        out["web_app_dns_domain"] = data["webAppDnsDomain"]
    if data.get("createdTime") is not None:
        import capo_supplychain.types._prelude.timestamp

        out["created_time"] = (
            capo_supplychain.types._prelude.timestamp.deserialize_json(
                data["createdTime"]
            )
        )
    if data.get("lastModifiedTime") is not None:
        import capo_supplychain.types._prelude.timestamp

        out["last_modified_time"] = (
            capo_supplychain.types._prelude.timestamp.deserialize_json(
                data["lastModifiedTime"]
            )
        )
    if data.get("instanceName") is not None:
        out["instance_name"] = data["instanceName"]
    if data.get("instanceDescription") is not None:
        out["instance_description"] = data["instanceDescription"]
    if data.get("kmsKeyArn") is not None:
        out["kms_key_arn"] = data["kmsKeyArn"]
    if data.get("versionNumber") is not None:
        out["version_number"] = float(data["versionNumber"])
    return out
