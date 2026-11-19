"""Generated from Smithy shape ``com.amazonaws.workspaces#CreateStandbyWorkspacesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.failed_create_standby_workspaces_request_list
    import capo_workspaces.types.pending_create_standby_workspaces_request_list


class CreateStandbyWorkspacesResult(TypedDict, closed=True):
    failed_standby_requests: NotRequired[
        "capo_workspaces.types.failed_create_standby_workspaces_request_list.FailedCreateStandbyWorkspacesRequestList"
    ]
    """<p>Information about the standby WorkSpace that could not be created. </p>"""
    pending_standby_requests: NotRequired[
        "capo_workspaces.types.pending_create_standby_workspaces_request_list.PendingCreateStandbyWorkspacesRequestList"
    ]
    """<p>Information about the standby WorkSpace that was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateStandbyWorkspacesResult) -> dict:
    out: dict = {}
    if "failed_standby_requests" in value:
        import capo_workspaces.types.failed_create_standby_workspaces_request_list

        out["FailedStandbyRequests"] = (
            capo_workspaces.types.failed_create_standby_workspaces_request_list.serialize_aws_json_1_1(
                value["failed_standby_requests"]
            )
        )
    if "pending_standby_requests" in value:
        import capo_workspaces.types.pending_create_standby_workspaces_request_list

        out["PendingStandbyRequests"] = (
            capo_workspaces.types.pending_create_standby_workspaces_request_list.serialize_aws_json_1_1(
                value["pending_standby_requests"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateStandbyWorkspacesResult:
    out: CreateStandbyWorkspacesResult = {}  # type: ignore[typeddict-item]
    if data.get("FailedStandbyRequests") is not None:
        import capo_workspaces.types.failed_create_standby_workspaces_request_list

        out["failed_standby_requests"] = (
            capo_workspaces.types.failed_create_standby_workspaces_request_list.deserialize_aws_json_1_1(
                data["FailedStandbyRequests"]
            )
        )
    if data.get("PendingStandbyRequests") is not None:
        import capo_workspaces.types.pending_create_standby_workspaces_request_list

        out["pending_standby_requests"] = (
            capo_workspaces.types.pending_create_standby_workspaces_request_list.deserialize_aws_json_1_1(
                data["PendingStandbyRequests"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateStandbyWorkspacesResult) -> dict:
    out: dict = {}
    if "failed_standby_requests" in value:
        import capo_workspaces.types.failed_create_standby_workspaces_request_list

        out["FailedStandbyRequests"] = (
            capo_workspaces.types.failed_create_standby_workspaces_request_list.serialize_cbor(
                value["failed_standby_requests"]
            )
        )
    if "pending_standby_requests" in value:
        import capo_workspaces.types.pending_create_standby_workspaces_request_list

        out["PendingStandbyRequests"] = (
            capo_workspaces.types.pending_create_standby_workspaces_request_list.serialize_cbor(
                value["pending_standby_requests"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> CreateStandbyWorkspacesResult:
    out: CreateStandbyWorkspacesResult = {}  # type: ignore[typeddict-item]
    if data.get("FailedStandbyRequests") is not None:
        import capo_workspaces.types.failed_create_standby_workspaces_request_list

        out["failed_standby_requests"] = (
            capo_workspaces.types.failed_create_standby_workspaces_request_list.deserialize_cbor(
                data["FailedStandbyRequests"]
            )
        )
    if data.get("PendingStandbyRequests") is not None:
        import capo_workspaces.types.pending_create_standby_workspaces_request_list

        out["pending_standby_requests"] = (
            capo_workspaces.types.pending_create_standby_workspaces_request_list.deserialize_cbor(
                data["PendingStandbyRequests"]
            )
        )
    return out
