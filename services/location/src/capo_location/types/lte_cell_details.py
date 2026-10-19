"""Generated from Smithy shape ``com.amazonaws.location#LteCellDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_location.types.eutran_cell_id
    import capo_location.types.lte_local_id
    import capo_location.types.lte_network_measurements_list
    import capo_location.types.rsrp
    import capo_location.types.rsrq


class LteCellDetails(TypedDict, closed=True):
    cell_id: "capo_location.types.eutran_cell_id.EutranCellId"
    """<p>The E-UTRAN Cell Identifier (ECI).</p>"""
    mcc: "int"
    """<p>The Mobile Country Code (MCC).</p>"""
    mnc: "int"
    """<p>The Mobile Network Code (MNC)</p>"""
    local_id: NotRequired["capo_location.types.lte_local_id.LteLocalId"]
    """<p>The LTE local identification information (local ID).</p>"""
    network_measurements: NotRequired[
        "capo_location.types.lte_network_measurements_list.LteNetworkMeasurementsList"
    ]
    """<p>The network measurements.</p>"""
    timing_advance: NotRequired["int"]
    """<p>Timing Advance (TA).</p>"""
    nr_capable: NotRequired["bool"]
    """<p>Indicates whether the LTE object is capable of supporting NR (new radio).</p>"""
    rsrp: NotRequired["capo_location.types.rsrp.Rsrp"]
    """<p>Signal power of the reference signal received, measured in decibel-milliwatts (dBm).</p>"""
    rsrq: NotRequired["capo_location.types.rsrq.Rsrq"]
    """<p>Signal quality of the reference Signal received, measured in decibels (dB).</p>"""
    tac: NotRequired["int"]
    """<p>LTE Tracking Area Code (TAC).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LteCellDetails) -> dict:
    out: dict = {}
    out["CellId"] = value.get("cell_id", 0)
    out["Mcc"] = value["mcc"]
    out["Mnc"] = value["mnc"]
    if "local_id" in value:
        import capo_location.types.lte_local_id

        out["LocalId"] = capo_location.types.lte_local_id.serialize_json(
            value["local_id"]
        )
    if "network_measurements" in value:
        import capo_location.types.lte_network_measurements_list

        out["NetworkMeasurements"] = (
            capo_location.types.lte_network_measurements_list.serialize_json(
                value["network_measurements"]
            )
        )
    if "timing_advance" in value:
        out["TimingAdvance"] = value["timing_advance"]
    if "nr_capable" in value:
        out["NrCapable"] = value["nr_capable"]
    if "rsrp" in value:
        out["Rsrp"] = value["rsrp"]
    if "rsrq" in value:
        out["Rsrq"] = (
            "NaN"
            if value["rsrq"] != value["rsrq"]
            else "Infinity"
            if value["rsrq"] == float("inf")
            else "-Infinity"
            if value["rsrq"] == float("-inf")
            else value["rsrq"]
        )
    if "tac" in value:
        out["Tac"] = value["tac"]
    return out


def deserialize_json(data: dict) -> LteCellDetails:
    out: LteCellDetails = {}  # type: ignore[typeddict-item]
    if data.get("CellId") is not None:
        out["cell_id"] = data["CellId"]
    else:
        out["cell_id"] = 0
    if data.get("Mcc") is not None:
        out["mcc"] = data["Mcc"]
    else:
        out["mcc"] = 0
    if data.get("Mnc") is not None:
        out["mnc"] = data["Mnc"]
    else:
        out["mnc"] = 0
    if data.get("LocalId") is not None:
        import capo_location.types.lte_local_id

        out["local_id"] = capo_location.types.lte_local_id.deserialize_json(
            data["LocalId"]
        )
    if data.get("NetworkMeasurements") is not None:
        import capo_location.types.lte_network_measurements_list

        out["network_measurements"] = (
            capo_location.types.lte_network_measurements_list.deserialize_json(
                data["NetworkMeasurements"]
            )
        )
    if data.get("TimingAdvance") is not None:
        out["timing_advance"] = data["TimingAdvance"]
    if data.get("NrCapable") is not None:
        out["nr_capable"] = data["NrCapable"]
    if data.get("Rsrp") is not None:
        out["rsrp"] = data["Rsrp"]
    if data.get("Rsrq") is not None:
        out["rsrq"] = float(data["Rsrq"])
    if data.get("Tac") is not None:
        out["tac"] = data["Tac"]
    return out
