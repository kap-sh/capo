"""Generated from Smithy shape ``com.amazonaws.rbin#RetentionPeriod``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_rbin.types.retention_period_unit
    import capo_rbin.types.retention_period_value


class RetentionPeriod(TypedDict, closed=True):
    retention_period_value: (
        "capo_rbin.types.retention_period_value.RetentionPeriodValue"
    )
    """<p>The period value for which the retention rule is to retain resources, measured in days. The supported retention periods are:</p> <ul> <li> <p>EBS volumes: 1 - 7 days</p> </li> <li> <p>EBS snapshots and EBS-backed AMIs: 1 - 365 days</p> </li> </ul>"""
    retention_period_unit: "capo_rbin.types.retention_period_unit.RetentionPeriodUnit"
    """<p>The unit of time in which the retention period is measured. Currently, only <code>DAYS</code> is supported.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RetentionPeriod) -> dict:
    out: dict = {}
    out["RetentionPeriodValue"] = value["retention_period_value"]
    import capo_rbin.types.retention_period_unit

    out["RetentionPeriodUnit"] = capo_rbin.types.retention_period_unit.serialize_json(
        value["retention_period_unit"]
    )
    return out


def deserialize_json(data: dict) -> RetentionPeriod:
    out: RetentionPeriod = {}  # type: ignore[typeddict-item]
    if data.get("RetentionPeriodValue") is not None:
        out["retention_period_value"] = data["RetentionPeriodValue"]
    else:
        out["retention_period_value"] = 0
    if data.get("RetentionPeriodUnit") is not None:
        import capo_rbin.types.retention_period_unit

        out["retention_period_unit"] = (
            capo_rbin.types.retention_period_unit.deserialize_json(
                data["RetentionPeriodUnit"]
            )
        )
    else:
        import typing

        out["retention_period_unit"] = typing.cast(
            "capo_rbin.types.retention_period_unit.RetentionPeriodUnit", ""
        )
    return out
