"""Generated from Smithy shape ``com.amazonaws.opensearch#UpdatePackageScopeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.package_id
    import capo_opensearch.types.package_scope_operation_enum
    import capo_opensearch.types.package_user_list


class UpdatePackageScopeRequest(TypedDict, closed=True):
    package_id: "capo_opensearch.types.package_id.PackageID"
    """<p>ID of the package whose scope is being updated.</p>"""
    operation: (
        "capo_opensearch.types.package_scope_operation_enum.PackageScopeOperationEnum"
    )
    """<p> The operation to perform on the package scope (e.g., add/remove/override users).</p>"""
    package_user_list: "capo_opensearch.types.package_user_list.PackageUserList"
    """<p> List of users to be added or removed from the package scope.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePackageScopeRequest) -> dict:
    out: dict = {}
    out["PackageID"] = value["package_id"]
    import capo_opensearch.types.package_scope_operation_enum

    out["Operation"] = (
        capo_opensearch.types.package_scope_operation_enum.serialize_json(
            value["operation"]
        )
    )
    import capo_opensearch.types.package_user_list

    out["PackageUserList"] = capo_opensearch.types.package_user_list.serialize_json(
        value["package_user_list"]
    )
    return out


def deserialize_json(data: dict) -> UpdatePackageScopeRequest:
    out: UpdatePackageScopeRequest = {}  # type: ignore[typeddict-item]
    if data.get("PackageID") is not None:
        out["package_id"] = data["PackageID"]
    else:
        out["package_id"] = ""
    if data.get("Operation") is not None:
        import capo_opensearch.types.package_scope_operation_enum

        out["operation"] = (
            capo_opensearch.types.package_scope_operation_enum.deserialize_json(
                data["Operation"]
            )
        )
    else:
        import typing

        out["operation"] = typing.cast(
            "capo_opensearch.types.package_scope_operation_enum.PackageScopeOperationEnum",
            "",
        )
    if data.get("PackageUserList") is not None:
        import capo_opensearch.types.package_user_list

        out["package_user_list"] = (
            capo_opensearch.types.package_user_list.deserialize_json(
                data["PackageUserList"]
            )
        )
    else:
        out["package_user_list"] = []
    return out
