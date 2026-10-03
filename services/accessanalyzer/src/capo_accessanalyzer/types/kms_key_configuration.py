"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#KmsKeyConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_accessanalyzer.types.kms_grant_configurations_list
    import capo_accessanalyzer.types.kms_key_policies_map


class KmsKeyConfiguration(TypedDict, closed=True):
    key_policies: NotRequired[
        "capo_accessanalyzer.types.kms_key_policies_map.KmsKeyPoliciesMap"
    ]
    """<p>Resource policy configuration for the KMS key. The only valid value for the name of the key policy is <code>default</code>. For more information, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html#key-policy-default">Default key policy</a>.</p>"""
    grants: NotRequired[
        "capo_accessanalyzer.types.kms_grant_configurations_list.KmsGrantConfigurationsList"
    ]
    """<p>A list of proposed grant configurations for the KMS key. If the proposed grant configuration is for an existing key, the access preview uses the proposed list of grant configurations in place of the existing grants. Otherwise, the access preview uses the existing grants for the key.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KmsKeyConfiguration) -> dict:
    out: dict = {}
    if "key_policies" in value:
        import capo_accessanalyzer.types.kms_key_policies_map

        out["keyPolicies"] = (
            capo_accessanalyzer.types.kms_key_policies_map.serialize_json(
                value["key_policies"]
            )
        )
    if "grants" in value:
        import capo_accessanalyzer.types.kms_grant_configurations_list

        out["grants"] = (
            capo_accessanalyzer.types.kms_grant_configurations_list.serialize_json(
                value["grants"]
            )
        )
    return out


def deserialize_json(data: dict) -> KmsKeyConfiguration:
    out: KmsKeyConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("keyPolicies") is not None:
        import capo_accessanalyzer.types.kms_key_policies_map

        out["key_policies"] = (
            capo_accessanalyzer.types.kms_key_policies_map.deserialize_json(
                data["keyPolicies"]
            )
        )
    if data.get("grants") is not None:
        import capo_accessanalyzer.types.kms_grant_configurations_list

        out["grants"] = (
            capo_accessanalyzer.types.kms_grant_configurations_list.deserialize_json(
                data["grants"]
            )
        )
    return out
