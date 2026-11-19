"""Generated from Smithy shape ``com.amazonaws.securityhub#Standard``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.boolean
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.standards_managed_by
    import capo_securityhub.types.standards_provider


class Standard(TypedDict, closed=True):
    standards_arn: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The ARN of the standard.</p>"""
    name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the standard.</p>"""
    description: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>A description of the standard.</p>"""
    enabled_by_default: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p>Whether the standard is enabled by default. When Security Hub CSPM is enabled from the console, if a standard is enabled by default, the check box for that standard is selected by default.</p> <p>When Security Hub CSPM is enabled using the <code>EnableSecurityHub</code> API operation, the standard is enabled by default unless <code>EnableDefaultStandards</code> is set to <code>false</code>.</p>"""
    provider: NotRequired["capo_securityhub.types.standards_provider.StandardsProvider"]
    """<p>The cloud provider whose resources the standard evaluates. For example, <code>AWS</code>, <code>Azure</code>, or <code>GCP</code>.</p>"""
    standards_managed_by: NotRequired[
        "capo_securityhub.types.standards_managed_by.StandardsManagedBy"
    ]
    """<p>Provides details about the management of a standard. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Standard) -> dict:
    out: dict = {}
    if "standards_arn" in value:
        out["StandardsArn"] = value["standards_arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "enabled_by_default" in value:
        out["EnabledByDefault"] = value["enabled_by_default"]
    if "provider" in value:
        import capo_securityhub.types.standards_provider

        out["Provider"] = capo_securityhub.types.standards_provider.serialize_json(
            value["provider"]
        )
    if "standards_managed_by" in value:
        import capo_securityhub.types.standards_managed_by

        out["StandardsManagedBy"] = (
            capo_securityhub.types.standards_managed_by.serialize_json(
                value["standards_managed_by"]
            )
        )
    return out


def deserialize_json(data: dict) -> Standard:
    out: Standard = {}  # type: ignore[typeddict-item]
    if data.get("StandardsArn") is not None:
        out["standards_arn"] = data["StandardsArn"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("EnabledByDefault") is not None:
        out["enabled_by_default"] = data["EnabledByDefault"]
    if data.get("Provider") is not None:
        import capo_securityhub.types.standards_provider

        out["provider"] = capo_securityhub.types.standards_provider.deserialize_json(
            data["Provider"]
        )
    if data.get("StandardsManagedBy") is not None:
        import capo_securityhub.types.standards_managed_by

        out["standards_managed_by"] = (
            capo_securityhub.types.standards_managed_by.deserialize_json(
                data["StandardsManagedBy"]
            )
        )
    return out
