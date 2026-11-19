"""Generated from Smithy shape ``com.amazonaws.controltower#EnabledBaselineFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_controltower.types.enabled_baseline_baseline_identifiers
    import capo_controltower.types.enabled_baseline_drift_statuses
    import capo_controltower.types.enabled_baseline_enablement_statuses
    import capo_controltower.types.enabled_baseline_parent_identifiers
    import capo_controltower.types.enabled_baseline_target_identifiers


class EnabledBaselineFilter(TypedDict, closed=True):
    target_identifiers: NotRequired[
        "capo_controltower.types.enabled_baseline_target_identifiers.EnabledBaselineTargetIdentifiers"
    ]
    """<p>Identifiers for the targets of the <code>Baseline</code> filter operation.</p>"""
    baseline_identifiers: NotRequired[
        "capo_controltower.types.enabled_baseline_baseline_identifiers.EnabledBaselineBaselineIdentifiers"
    ]
    """<p>Identifiers for the <code>Baseline</code> objects returned as part of the filter operation.</p>"""
    parent_identifiers: NotRequired[
        "capo_controltower.types.enabled_baseline_parent_identifiers.EnabledBaselineParentIdentifiers"
    ]
    """<p>An optional filter that sets up a list of <code>parentIdentifiers</code> to filter the results of the <code>ListEnabledBaseline</code> output.</p>"""
    statuses: NotRequired[
        "capo_controltower.types.enabled_baseline_enablement_statuses.EnabledBaselineEnablementStatuses"
    ]
    """<p>A list of <code>EnablementStatus</code> items.</p>"""
    inheritance_drift_statuses: NotRequired[
        "capo_controltower.types.enabled_baseline_drift_statuses.EnabledBaselineDriftStatuses"
    ]
    """<p>A list of <code>EnabledBaselineDriftStatus</code> items for enabled baselines.</p>"""
    source_drift_statuses: NotRequired[
        "capo_controltower.types.enabled_baseline_drift_statuses.EnabledBaselineDriftStatuses"
    ]
    """<p>A list of <code>EnabledBaselineDriftStatus</code> items for enabled baselines.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnabledBaselineFilter) -> dict:
    out: dict = {}
    if "target_identifiers" in value:
        import capo_controltower.types.enabled_baseline_target_identifiers

        out["targetIdentifiers"] = (
            capo_controltower.types.enabled_baseline_target_identifiers.serialize_json(
                value["target_identifiers"]
            )
        )
    if "baseline_identifiers" in value:
        import capo_controltower.types.enabled_baseline_baseline_identifiers

        out["baselineIdentifiers"] = (
            capo_controltower.types.enabled_baseline_baseline_identifiers.serialize_json(
                value["baseline_identifiers"]
            )
        )
    if "parent_identifiers" in value:
        import capo_controltower.types.enabled_baseline_parent_identifiers

        out["parentIdentifiers"] = (
            capo_controltower.types.enabled_baseline_parent_identifiers.serialize_json(
                value["parent_identifiers"]
            )
        )
    if "statuses" in value:
        import capo_controltower.types.enabled_baseline_enablement_statuses

        out["statuses"] = (
            capo_controltower.types.enabled_baseline_enablement_statuses.serialize_json(
                value["statuses"]
            )
        )
    if "inheritance_drift_statuses" in value:
        import capo_controltower.types.enabled_baseline_drift_statuses

        out["inheritanceDriftStatuses"] = (
            capo_controltower.types.enabled_baseline_drift_statuses.serialize_json(
                value["inheritance_drift_statuses"]
            )
        )
    if "source_drift_statuses" in value:
        import capo_controltower.types.enabled_baseline_drift_statuses

        out["sourceDriftStatuses"] = (
            capo_controltower.types.enabled_baseline_drift_statuses.serialize_json(
                value["source_drift_statuses"]
            )
        )
    return out


def deserialize_json(data: dict) -> EnabledBaselineFilter:
    out: EnabledBaselineFilter = {}  # type: ignore[typeddict-item]
    if data.get("targetIdentifiers") is not None:
        import capo_controltower.types.enabled_baseline_target_identifiers

        out["target_identifiers"] = (
            capo_controltower.types.enabled_baseline_target_identifiers.deserialize_json(
                data["targetIdentifiers"]
            )
        )
    if data.get("baselineIdentifiers") is not None:
        import capo_controltower.types.enabled_baseline_baseline_identifiers

        out["baseline_identifiers"] = (
            capo_controltower.types.enabled_baseline_baseline_identifiers.deserialize_json(
                data["baselineIdentifiers"]
            )
        )
    if data.get("parentIdentifiers") is not None:
        import capo_controltower.types.enabled_baseline_parent_identifiers

        out["parent_identifiers"] = (
            capo_controltower.types.enabled_baseline_parent_identifiers.deserialize_json(
                data["parentIdentifiers"]
            )
        )
    if data.get("statuses") is not None:
        import capo_controltower.types.enabled_baseline_enablement_statuses

        out["statuses"] = (
            capo_controltower.types.enabled_baseline_enablement_statuses.deserialize_json(
                data["statuses"]
            )
        )
    if data.get("inheritanceDriftStatuses") is not None:
        import capo_controltower.types.enabled_baseline_drift_statuses

        out["inheritance_drift_statuses"] = (
            capo_controltower.types.enabled_baseline_drift_statuses.deserialize_json(
                data["inheritanceDriftStatuses"]
            )
        )
    if data.get("sourceDriftStatuses") is not None:
        import capo_controltower.types.enabled_baseline_drift_statuses

        out["source_drift_statuses"] = (
            capo_controltower.types.enabled_baseline_drift_statuses.deserialize_json(
                data["sourceDriftStatuses"]
            )
        )
    return out
