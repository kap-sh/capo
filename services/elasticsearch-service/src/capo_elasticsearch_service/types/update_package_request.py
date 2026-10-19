"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#UpdatePackageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticsearch_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.commit_message
    import capo_elasticsearch_service.types.package_description
    import capo_elasticsearch_service.types.package_id
    import capo_elasticsearch_service.types.package_source


class UpdatePackageRequest(TypedDict, closed=True):
    package_id: "capo_elasticsearch_service.types.package_id.PackageID"
    """<p>Unique identifier for the package.</p>"""
    package_source: "capo_elasticsearch_service.types.package_source.PackageSource"
    package_description: NotRequired[
        "capo_elasticsearch_service.types.package_description.PackageDescription"
    ]
    """<p>New description of the package.</p>"""
    commit_message: NotRequired[
        "capo_elasticsearch_service.types.commit_message.CommitMessage"
    ]
    """<p>An info message for the new version which will be shown as part of <code>GetPackageVersionHistoryResponse</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePackageRequest) -> dict:
    out: dict = {}
    out["PackageID"] = value["package_id"]
    import capo_elasticsearch_service.types.package_source

    out["PackageSource"] = (
        capo_elasticsearch_service.types.package_source.serialize_json(
            value["package_source"]
        )
    )
    if "package_description" in value:
        out["PackageDescription"] = value["package_description"]
    if "commit_message" in value:
        out["CommitMessage"] = value["commit_message"]
    return out


def deserialize_json(data: dict) -> UpdatePackageRequest:
    out: UpdatePackageRequest = {}  # type: ignore[typeddict-item]
    if data.get("PackageID") is not None:
        out["package_id"] = data["PackageID"]
    else:
        out["package_id"] = ""
    if data.get("PackageSource") is not None:
        import capo_elasticsearch_service.types.package_source

        out["package_source"] = (
            capo_elasticsearch_service.types.package_source.deserialize_json(
                data["PackageSource"]
            )
        )
    else:
        raise DeserializationError("UpdatePackageRequest.package_source required")
    if data.get("PackageDescription") is not None:
        out["package_description"] = data["PackageDescription"]
    if data.get("CommitMessage") is not None:
        out["commit_message"] = data["CommitMessage"]
    return out
