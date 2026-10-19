"""Generated from Smithy shape ``com.amazonaws.lakeformation#ExternalFilteringConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lakeformation.types.enable_status
    import capo_lakeformation.types.scope_targets


class ExternalFilteringConfiguration(TypedDict, closed=True):
    status: "capo_lakeformation.types.enable_status.EnableStatus"
    """<p>Allows to enable or disable the third-party applications that are allowed to access data managed by Lake Formation.</p>"""
    authorized_targets: "capo_lakeformation.types.scope_targets.ScopeTargets"
    """<p>List of third-party application <code>ARNs</code> integrated with Lake Formation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExternalFilteringConfiguration) -> dict:
    out: dict = {}
    import capo_lakeformation.types.enable_status

    out["Status"] = capo_lakeformation.types.enable_status.serialize_json(
        value["status"]
    )
    import capo_lakeformation.types.scope_targets

    out["AuthorizedTargets"] = capo_lakeformation.types.scope_targets.serialize_json(
        value["authorized_targets"]
    )
    return out


def deserialize_json(data: dict) -> ExternalFilteringConfiguration:
    out: ExternalFilteringConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Status") is not None:
        import capo_lakeformation.types.enable_status

        out["status"] = capo_lakeformation.types.enable_status.deserialize_json(
            data["Status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_lakeformation.types.enable_status.EnableStatus", ""
        )
    if data.get("AuthorizedTargets") is not None:
        import capo_lakeformation.types.scope_targets

        out["authorized_targets"] = (
            capo_lakeformation.types.scope_targets.deserialize_json(
                data["AuthorizedTargets"]
            )
        )
    else:
        out["authorized_targets"] = []
    return out
