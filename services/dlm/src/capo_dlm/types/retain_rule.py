"""Generated from Smithy shape ``com.amazonaws.dlm#RetainRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dlm.types.retention_interval_unit_values
    import capo_dlm.types.standard_tier_retain_rule_count
    import capo_dlm.types.standard_tier_retain_rule_interval


class RetainRule(TypedDict, closed=True):
    count: NotRequired[
        "capo_dlm.types.standard_tier_retain_rule_count.StandardTierRetainRuleCount"
    ]
    """<p>The number of snapshots to retain for each volume, up to a maximum of 1000. For example if you want to retain a maximum of three snapshots, specify <code>3</code>. When the fourth snapshot is created, the oldest retained snapshot is deleted, or it is moved to the archive tier if you have specified an <a href="https://docs.aws.amazon.com/dlm/latest/APIReference/API_ArchiveRule.html">ArchiveRule</a>.</p>"""
    interval: NotRequired[
        "capo_dlm.types.standard_tier_retain_rule_interval.StandardTierRetainRuleInterval"
    ]
    """<p>The amount of time to retain each snapshot. The maximum is 100 years. This is equivalent to 1200 months, 5200 weeks, or 36500 days.</p>"""
    interval_unit: NotRequired[
        "capo_dlm.types.retention_interval_unit_values.RetentionIntervalUnitValues"
    ]
    """<p>The unit of time for time-based retention. For example, to retain snapshots for 3 months, specify <code>Interval=3</code> and <code>IntervalUnit=MONTHS</code>. Once the snapshot has been retained for 3 months, it is deleted, or it is moved to the archive tier if you have specified an <a href="https://docs.aws.amazon.com/dlm/latest/APIReference/API_ArchiveRule.html">ArchiveRule</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RetainRule) -> dict:
    out: dict = {}
    if "count" in value:
        out["Count"] = value["count"]
    if "interval" in value:
        out["Interval"] = value["interval"]
    if "interval_unit" in value:
        import capo_dlm.types.retention_interval_unit_values

        out["IntervalUnit"] = (
            capo_dlm.types.retention_interval_unit_values.serialize_json(
                value["interval_unit"]
            )
        )
    return out


def deserialize_json(data: dict) -> RetainRule:
    out: RetainRule = {}  # type: ignore[typeddict-item]
    if data.get("Count") is not None:
        out["count"] = data["Count"]
    if data.get("Interval") is not None:
        out["interval"] = data["Interval"]
    if data.get("IntervalUnit") is not None:
        import capo_dlm.types.retention_interval_unit_values

        out["interval_unit"] = (
            capo_dlm.types.retention_interval_unit_values.deserialize_json(
                data["IntervalUnit"]
            )
        )
    return out
