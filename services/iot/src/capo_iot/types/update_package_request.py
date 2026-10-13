"""Generated from Smithy shape ``com.amazonaws.iot#UpdatePackageRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.client_token
    import capo_iot.types.package_name
    import capo_iot.types.resource_description
    import capo_iot.types.unset_default_version
    import capo_iot.types.version_name


class UpdatePackageRequest(TypedDict, closed=True):
    package_name: "capo_iot.types.package_name.PackageName"
    """<p>The name of the target software package.</p>"""
    description: NotRequired["capo_iot.types.resource_description.ResourceDescription"]
    """<p>The package description.</p>"""
    default_version_name: NotRequired["capo_iot.types.version_name.VersionName"]
    """<p>The name of the default package version.</p> <p> <b>Note:</b> You cannot name a <code>defaultVersion</code> and set <code>unsetDefaultVersion</code> equal to <code>true</code> at the same time.</p>"""
    unset_default_version: NotRequired[
        "capo_iot.types.unset_default_version.UnsetDefaultVersion"
    ]
    """<p>Indicates whether you want to remove the named default package version from the software package. Set as <code>true</code> to remove the default package version. </p> <p> <b>Note:</b> You cannot name a <code>defaultVersion</code> and set <code>unsetDefaultVersion</code> equal to <code>true</code> at the same time.</p>"""
    client_token: NotRequired["capo_iot.types.client_token.ClientToken"]
    """<p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePackageRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    if "default_version_name" in value:
        out["defaultVersionName"] = value["default_version_name"]
    if "unset_default_version" in value:
        out["unsetDefaultVersion"] = value["unset_default_version"]
    return out


def deserialize_json(data: dict) -> UpdatePackageRequest:
    out: UpdatePackageRequest = {}  # type: ignore[typeddict-item]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("defaultVersionName") is not None:
        out["default_version_name"] = data["defaultVersionName"]
    if data.get("unsetDefaultVersion") is not None:
        out["unset_default_version"] = data["unsetDefaultVersion"]
    return out


def redact_sensitive(value: UpdatePackageRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
