"""Generated from Smithy shape ``com.amazonaws.appfabric#BatchGetUserAccessTasksResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appfabric.types.user_access_results_list


class BatchGetUserAccessTasksResponse(TypedDict, closed=True):
    user_access_results_list: NotRequired[
        "capo_appfabric.types.user_access_results_list.UserAccessResultsList"
    ]
    """<p>Contains a list of user access results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetUserAccessTasksResponse) -> dict:
    out: dict = {}
    if "user_access_results_list" in value:
        import capo_appfabric.types.user_access_results_list

        out["userAccessResultsList"] = (
            capo_appfabric.types.user_access_results_list.serialize_json(
                value["user_access_results_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchGetUserAccessTasksResponse:
    out: BatchGetUserAccessTasksResponse = {}  # type: ignore[typeddict-item]
    if data.get("userAccessResultsList") is not None:
        import capo_appfabric.types.user_access_results_list

        out["user_access_results_list"] = (
            capo_appfabric.types.user_access_results_list.deserialize_json(
                data["userAccessResultsList"]
            )
        )
    return out


def redact_sensitive(value: BatchGetUserAccessTasksResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "user_access_results_list" in value:
        import capo_appfabric.types.user_access_results_list

        out["user_access_results_list"] = (
            capo_appfabric.types.user_access_results_list.redact_sensitive(
                value["user_access_results_list"]
            )
        )
    return out
