"""Generated from Smithy shape ``com.amazonaws.iotwireless#CdmaObj``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.base_lat
    import capo_iot_wireless.types.base_lng
    import capo_iot_wireless.types.base_station_id
    import capo_iot_wireless.types.cdma_local_id
    import capo_iot_wireless.types.cdma_nmr_list
    import capo_iot_wireless.types.network_id
    import capo_iot_wireless.types.pilot_power
    import capo_iot_wireless.types.registration_zone
    import capo_iot_wireless.types.system_id


class CdmaObj(TypedDict, closed=True):
    system_id: "capo_iot_wireless.types.system_id.SystemId"
    """<p>CDMA system ID (SID).</p>"""
    network_id: "capo_iot_wireless.types.network_id.NetworkId"
    """<p>CDMA network ID (NID).</p>"""
    base_station_id: "capo_iot_wireless.types.base_station_id.BaseStationId"
    """<p>CDMA base station ID (BSID).</p>"""
    registration_zone: NotRequired[
        "capo_iot_wireless.types.registration_zone.RegistrationZone"
    ]
    """<p>CDMA registration zone (RZ).</p>"""
    cdma_local_id: NotRequired["capo_iot_wireless.types.cdma_local_id.CdmaLocalId"]
    """<p>CDMA local identification (local ID) parameters.</p>"""
    pilot_power: NotRequired["capo_iot_wireless.types.pilot_power.PilotPower"]
    """<p>Transmit power level of the pilot signal, measured in dBm (decibel-milliwatts).</p>"""
    base_lat: NotRequired["capo_iot_wireless.types.base_lat.BaseLat"]
    """<p>CDMA base station latitude in degrees.</p>"""
    base_lng: NotRequired["capo_iot_wireless.types.base_lng.BaseLng"]
    """<p>CDMA base station longitude in degrees.</p>"""
    cdma_nmr: NotRequired["capo_iot_wireless.types.cdma_nmr_list.CdmaNmrList"]
    """<p>CDMA network measurement reports.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CdmaObj) -> dict:
    out: dict = {}
    out["SystemId"] = value["system_id"]
    out["NetworkId"] = value["network_id"]
    out["BaseStationId"] = value["base_station_id"]
    if "registration_zone" in value:
        out["RegistrationZone"] = value["registration_zone"]
    if "cdma_local_id" in value:
        import capo_iot_wireless.types.cdma_local_id

        out["CdmaLocalId"] = capo_iot_wireless.types.cdma_local_id.serialize_json(
            value["cdma_local_id"]
        )
    if "pilot_power" in value:
        out["PilotPower"] = value["pilot_power"]
    if "base_lat" in value:
        out["BaseLat"] = (
            "NaN"
            if value["base_lat"] != value["base_lat"]
            else "Infinity"
            if value["base_lat"] == float("inf")
            else "-Infinity"
            if value["base_lat"] == float("-inf")
            else value["base_lat"]
        )
    if "base_lng" in value:
        out["BaseLng"] = (
            "NaN"
            if value["base_lng"] != value["base_lng"]
            else "Infinity"
            if value["base_lng"] == float("inf")
            else "-Infinity"
            if value["base_lng"] == float("-inf")
            else value["base_lng"]
        )
    if "cdma_nmr" in value:
        import capo_iot_wireless.types.cdma_nmr_list

        out["CdmaNmr"] = capo_iot_wireless.types.cdma_nmr_list.serialize_json(
            value["cdma_nmr"]
        )
    return out


def deserialize_json(data: dict) -> CdmaObj:
    out: CdmaObj = {}  # type: ignore[typeddict-item]
    if data.get("SystemId") is not None:
        out["system_id"] = data["SystemId"]
    else:
        out["system_id"] = 0
    if data.get("NetworkId") is not None:
        out["network_id"] = data["NetworkId"]
    else:
        out["network_id"] = 0
    if data.get("BaseStationId") is not None:
        out["base_station_id"] = data["BaseStationId"]
    else:
        out["base_station_id"] = 0
    if data.get("RegistrationZone") is not None:
        out["registration_zone"] = data["RegistrationZone"]
    if data.get("CdmaLocalId") is not None:
        import capo_iot_wireless.types.cdma_local_id

        out["cdma_local_id"] = capo_iot_wireless.types.cdma_local_id.deserialize_json(
            data["CdmaLocalId"]
        )
    if data.get("PilotPower") is not None:
        out["pilot_power"] = data["PilotPower"]
    if data.get("BaseLat") is not None:
        out["base_lat"] = float(data["BaseLat"])
    if data.get("BaseLng") is not None:
        out["base_lng"] = float(data["BaseLng"])
    if data.get("CdmaNmr") is not None:
        import capo_iot_wireless.types.cdma_nmr_list

        out["cdma_nmr"] = capo_iot_wireless.types.cdma_nmr_list.deserialize_json(
            data["CdmaNmr"]
        )
    return out
