"""Generated from Smithy shape ``com.amazonaws.inspector2#FreeTrialInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_inspector2.types.cloud_provider
    import capo_inspector2.types.free_trial_status
    import capo_inspector2.types.free_trial_type


class FreeTrialInfo(TypedDict, closed=True):
    type: "capo_inspector2.types.free_trial_type.FreeTrialType"
    """<p>The type of scan covered by the Amazon Inspector free trail.</p>"""
    start: "datetime.datetime"
    """<p>The date and time that the Amazon Inspector free trail started for a given account.</p>"""
    end: "datetime.datetime"
    """<p>The date and time that the Amazon Inspector free trail ends for a given account.</p>"""
    status: "capo_inspector2.types.free_trial_status.FreeTrialStatus"
    """<p>The order to sort results by.</p>"""
    cloud_provider: NotRequired["capo_inspector2.types.cloud_provider.CloudProvider"]
    """<p>The cloud provider associated with the free trial information.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FreeTrialInfo) -> dict:
    out: dict = {}
    out["type"] = value["type"]
    import capo_inspector2.types._prelude.timestamp

    out["start"] = capo_inspector2.types._prelude.timestamp.serialize_json(
        value["start"]
    )
    import capo_inspector2.types._prelude.timestamp

    out["end"] = capo_inspector2.types._prelude.timestamp.serialize_json(value["end"])
    out["status"] = value["status"]
    if "cloud_provider" in value:
        out["cloudProvider"] = value["cloud_provider"]
    return out


def deserialize_json(data: dict) -> FreeTrialInfo:
    out: FreeTrialInfo = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        out["type"] = ""
    if data.get("start") is not None:
        import capo_inspector2.types._prelude.timestamp

        out["start"] = capo_inspector2.types._prelude.timestamp.deserialize_json(
            data["start"]
        )
    else:
        import datetime

        out["start"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("end") is not None:
        import capo_inspector2.types._prelude.timestamp

        out["end"] = capo_inspector2.types._prelude.timestamp.deserialize_json(
            data["end"]
        )
    else:
        import datetime

        out["end"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        out["status"] = ""
    if data.get("cloudProvider") is not None:
        out["cloud_provider"] = data["cloudProvider"]
    return out
