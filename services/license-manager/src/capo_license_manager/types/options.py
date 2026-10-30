"""Generated from Smithy shape ``com.amazonaws.licensemanager#Options``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_license_manager.types.activation_override_behavior
    import capo_license_manager.types.grant_status


class Options(TypedDict, closed=True):
    activation_override_behavior: NotRequired[
        "capo_license_manager.types.activation_override_behavior.ActivationOverrideBehavior"
    ]
    """<p>An activation option for your grant that determines the behavior of activating a grant. Activation options can only be used with granted licenses sourced from the Amazon Web Services Marketplace. Additionally, the operation must activate the grant. For the <code>CreateGrantVersion</code> operation, specify <code>ACTIVE</code> for the <code>Status</code> parameter. For the <code>CreateGrant</code> operation, specify <code>ACTIVE</code> for the <code>DesiredStatus</code> option.</p> <ul> <li> <p>As a license administrator, you can optionally specify an <code>ActivationOverrideBehavior</code> when activating a grant.</p> </li> <li> <p>As a grantor, you can optionally specify an <code>ActivationOverrideBehavior</code> when you activate a grant for a grantee account in your organization.</p> </li> <li> <p>As a grantee, if the grantor creating the distributed grant doesn’t specify an <code>ActivationOverrideBehavior</code>, you can optionally specify one when you are activating the grant.</p> </li> </ul> <dl> <dt>DISTRIBUTED_GRANTS_ONLY</dt> <dd> <p>Use this value to activate a grant without replacing any member account’s active grants for the same product.</p> </dd> <dt>ALL_GRANTS_PERMITTED_BY_ISSUER</dt> <dd> <p>Use this value to activate a grant and disable other active grants in any member accounts for the same product. This action will also replace their previously activated grants with this activated grant.</p> </dd> </dl>"""
    desired_status: NotRequired["capo_license_manager.types.grant_status.GrantStatus"]
    """<p>The status of the grant after License Manager creates it. The only supported value is <code>ACTIVE</code>. Specify <code>ACTIVE</code> to create and activate the grant in one request.</p> <p>You can specify this option only for the <code>CreateGrant</code> operation, and only when the grant principal is an organization or an organizational unit (OU). To change the status of an existing grant, use the <code>Status</code> parameter of the <code>CreateGrantVersion</code> operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Options) -> dict:
    out: dict = {}
    if "activation_override_behavior" in value:
        import capo_license_manager.types.activation_override_behavior

        out["ActivationOverrideBehavior"] = (
            capo_license_manager.types.activation_override_behavior.serialize_aws_json_1_1(
                value["activation_override_behavior"]
            )
        )
    if "desired_status" in value:
        import capo_license_manager.types.grant_status

        out["DesiredStatus"] = (
            capo_license_manager.types.grant_status.serialize_aws_json_1_1(
                value["desired_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Options:
    out: Options = {}  # type: ignore[typeddict-item]
    if data.get("ActivationOverrideBehavior") is not None:
        import capo_license_manager.types.activation_override_behavior

        out["activation_override_behavior"] = (
            capo_license_manager.types.activation_override_behavior.deserialize_aws_json_1_1(
                data["ActivationOverrideBehavior"]
            )
        )
    if data.get("DesiredStatus") is not None:
        import capo_license_manager.types.grant_status

        out["desired_status"] = (
            capo_license_manager.types.grant_status.deserialize_aws_json_1_1(
                data["DesiredStatus"]
            )
        )
    return out
