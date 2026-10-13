"""Generated from Smithy shape ``com.amazonaws.devicefarm#ListTestGridSessionArtifactsResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_device_farm.types.pagination_token
    import capo_device_farm.types.test_grid_session_artifacts


class ListTestGridSessionArtifactsResult(TypedDict, closed=True):
    artifacts: NotRequired[
        "capo_device_farm.types.test_grid_session_artifacts.TestGridSessionArtifacts"
    ]
    """<p>A list of test grid session artifacts for a <a>TestGridSession</a>.</p>"""
    next_token: NotRequired["capo_device_farm.types.pagination_token.PaginationToken"]
    """<p>Pagination token.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTestGridSessionArtifactsResult) -> dict:
    out: dict = {}
    if "artifacts" in value:
        import capo_device_farm.types.test_grid_session_artifacts

        out["artifacts"] = (
            capo_device_farm.types.test_grid_session_artifacts.serialize_aws_json_1_1(
                value["artifacts"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTestGridSessionArtifactsResult:
    out: ListTestGridSessionArtifactsResult = {}  # type: ignore[typeddict-item]
    if data.get("artifacts") is not None:
        import capo_device_farm.types.test_grid_session_artifacts

        out["artifacts"] = (
            capo_device_farm.types.test_grid_session_artifacts.deserialize_aws_json_1_1(
                data["artifacts"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: ListTestGridSessionArtifactsResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "artifacts" in value:
        import capo_device_farm.types.test_grid_session_artifacts

        out["artifacts"] = (
            capo_device_farm.types.test_grid_session_artifacts.redact_sensitive(
                value["artifacts"]
            )
        )
    return out
