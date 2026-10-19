"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#DeletePolicyStoreAliasInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.alias
    import capo_verifiedpermissions.types.deletion_mode


class DeletePolicyStoreAliasInput(TypedDict, closed=True):
    alias_name: "capo_verifiedpermissions.types.alias.Alias"
    """<p>Specifies the name of the policy store alias that you want to delete.</p> <note> <p>The alias name must always be prefixed with <code>policy-store-alias/</code>.</p> </note>"""
    deletion_mode: NotRequired[
        "capo_verifiedpermissions.types.deletion_mode.DeletionMode"
    ]
    """<p>Specifies the deletion mode for the policy store alias. The valid values are:</p> <ul> <li> <p> <b>SoftDelete</b> – The policy store alias enters the <code>PendingDeletion</code> state. This is the default behavior when no <code>deletionMode</code> is specified.</p> </li> <li> <p> <b>HardDelete</b> – The policy store alias is immediately deleted, bypassing the <code>PendingDeletion</code> state.</p> </li> </ul>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeletePolicyStoreAliasInput) -> dict:
    out: dict = {}
    out["aliasName"] = value["alias_name"]
    if "deletion_mode" in value:
        import capo_verifiedpermissions.types.deletion_mode

        out["deletionMode"] = (
            capo_verifiedpermissions.types.deletion_mode.serialize_aws_json_1_0(
                value["deletion_mode"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DeletePolicyStoreAliasInput:
    out: DeletePolicyStoreAliasInput = {}  # type: ignore[typeddict-item]
    if data.get("aliasName") is not None:
        out["alias_name"] = data["aliasName"]
    else:
        out["alias_name"] = ""
    if data.get("deletionMode") is not None:
        import capo_verifiedpermissions.types.deletion_mode

        out["deletion_mode"] = (
            capo_verifiedpermissions.types.deletion_mode.deserialize_aws_json_1_0(
                data["deletionMode"]
            )
        )
    return out
