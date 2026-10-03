"""Generated from Smithy shape ``com.amazonaws.pcs#AccountingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_pcs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_pcs.types.accounting_mode


class AccountingRequest(TypedDict, closed=True):
    default_purge_time_in_days: NotRequired["int"]
    """<p>The default value for all purge settings for <code>slurmdbd.conf</code>. For more information, see the <a href="https://slurm.schedmd.com/slurmdbd.conf.html">slurmdbd.conf documentation at SchedMD</a>.</p> <p>The default value for <code>defaultPurgeTimeInDays</code> is <code>-1</code>.</p> <p>A value of <code>-1</code> means there is no purge time and records persist as long as the cluster exists.</p> <important> <p> <code>0</code> isn't a valid value.</p> </important>"""
    mode: "capo_pcs.types.accounting_mode.AccountingMode"
    """<p>The default value for <code>mode</code> is <code>NONE</code>. A value of <code>STANDARD</code> means Slurm accounting is enabled.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AccountingRequest) -> dict:
    out: dict = {}
    if "default_purge_time_in_days" in value:
        out["defaultPurgeTimeInDays"] = value["default_purge_time_in_days"]
    import capo_pcs.types.accounting_mode

    out["mode"] = capo_pcs.types.accounting_mode.serialize_aws_json_1_0(value["mode"])
    return out


def deserialize_aws_json_1_0(data: dict) -> AccountingRequest:
    out: AccountingRequest = {}  # type: ignore[typeddict-item]
    if data.get("defaultPurgeTimeInDays") is not None:
        out["default_purge_time_in_days"] = data["defaultPurgeTimeInDays"]
    if data.get("mode") is not None:
        import capo_pcs.types.accounting_mode

        out["mode"] = capo_pcs.types.accounting_mode.deserialize_aws_json_1_0(
            data["mode"]
        )
    else:
        raise DeserializationError("AccountingRequest.mode required")
    return out
