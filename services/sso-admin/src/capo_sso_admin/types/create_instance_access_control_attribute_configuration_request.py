"""Generated from Smithy shape ``com.amazonaws.ssoadmin#CreateInstanceAccessControlAttributeConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_sso_admin.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sso_admin.types.instance_access_control_attribute_configuration
    import capo_sso_admin.types.instance_arn


class CreateInstanceAccessControlAttributeConfigurationRequest(TypedDict, closed=True):
    instance_arn: "capo_sso_admin.types.instance_arn.InstanceArn"
    """<p>The ARN of the IAM Identity Center instance under which the operation will be executed.</p>"""
    instance_access_control_attribute_configuration: "capo_sso_admin.types.instance_access_control_attribute_configuration.InstanceAccessControlAttributeConfiguration"
    """<p>Specifies the IAM Identity Center identity store attributes to add to your ABAC configuration. When using an external identity provider as an identity source, you can pass attributes through the SAML assertion. Doing so provides an alternative to configuring attributes from the IAM Identity Center identity store. If a SAML assertion passes any of these attributes, IAM Identity Center will replace the attribute value with the value from the IAM Identity Center identity store.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: CreateInstanceAccessControlAttributeConfigurationRequest,
) -> dict:
    out: dict = {}
    out["InstanceArn"] = value["instance_arn"]
    import capo_sso_admin.types.instance_access_control_attribute_configuration

    out["InstanceAccessControlAttributeConfiguration"] = (
        capo_sso_admin.types.instance_access_control_attribute_configuration.serialize_aws_json_1_1(
            value["instance_access_control_attribute_configuration"]
        )
    )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> CreateInstanceAccessControlAttributeConfigurationRequest:
    out: CreateInstanceAccessControlAttributeConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("InstanceArn") is not None:
        out["instance_arn"] = data["InstanceArn"]
    else:
        out["instance_arn"] = ""
    if data.get("InstanceAccessControlAttributeConfiguration") is not None:
        import capo_sso_admin.types.instance_access_control_attribute_configuration

        out["instance_access_control_attribute_configuration"] = (
            capo_sso_admin.types.instance_access_control_attribute_configuration.deserialize_aws_json_1_1(
                data["InstanceAccessControlAttributeConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "CreateInstanceAccessControlAttributeConfigurationRequest.instance_access_control_attribute_configuration required"
        )
    return out
