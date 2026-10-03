"""Generated from Smithy shape ``com.amazonaws.macie2#ClassificationResultStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_macie2.types.__string


class ClassificationResultStatus(TypedDict, closed=True):
    code: NotRequired["capo_macie2.types.__string.__string"]
    """<p>The status of the finding. Possible values are:</p> <ul><li><p>COMPLETE - Amazon Macie successfully completed its analysis of the S3 object that the finding applies to.</p></li> <li><p>PARTIAL - Macie analyzed only a subset of the data in the S3 object that the finding applies to. For example, the object is an archive file that contains files in an unsupported format.</p></li> <li><p>SKIPPED - Macie wasn't able to analyze the S3 object that the finding applies to. For example, the object is a file that uses an unsupported format.</p></li></ul>"""
    reason: NotRequired["capo_macie2.types.__string.__string"]
    """<p>A brief description of the status of the finding. This value is null if the status (code) of the finding is COMPLETE.</p> <p>Amazon Macie uses this value to notify you of any errors, warnings, or considerations that might impact your analysis of the finding and the affected S3 object. Possible values are:</p> <ul><li><p>ARCHIVE_CONTAINS_UNPROCESSED_FILES - The object is an archive file and Macie extracted and analyzed only some or none of the files in the archive. To determine which files Macie analyzed, if any, refer to the corresponding sensitive data discovery result for the finding (classificationDetails.detailedResultsLocation).</p></li> <li><p>ARCHIVE_EXCEEDS_SIZE_LIMIT - The object is an archive file whose total storage size exceeds the size quota for this type of archive.</p></li> <li><p>ARCHIVE_NESTING_LEVEL_OVER_LIMIT - The object is an archive file whose nested depth exceeds the quota for the maximum number of nested levels that Macie analyzes for this type of archive.</p></li> <li><p>ARCHIVE_TOTAL_BYTES_EXTRACTED_OVER_LIMIT - The object is an archive file that exceeds the quota for the maximum amount of data that Macie extracts and analyzes for this type of archive.</p></li> <li><p>ARCHIVE_TOTAL_DOCUMENTS_PROCESSED_OVER_LIMIT - The object is an archive file that contains more than the maximum number of files that Macie extracts and analyzes for this type of archive.</p></li> <li><p>FILE_EXCEEDS_SIZE_LIMIT - The storage size of the object exceeds the size quota for this type of file.</p></li> <li><p>INVALID_ENCRYPTION - The object is encrypted using server-side encryption but Macie isn't allowed to use the key. Macie can't decrypt and analyze the object.</p></li> <li><p>INVALID_KMS_KEY - The object is encrypted with an KMS key that was disabled or is being deleted. Macie can't decrypt and analyze the object.</p></li> <li><p>INVALID_OBJECT_STATE - The object doesn't use a supported Amazon S3 storage class.</p></li> <li><p>JSON_NESTING_LEVEL_OVER_LIMIT - The object contains JSON data and the nested depth of the data exceeds the quota for the number of nested levels that Macie analyzes for this type of file.</p></li> <li><p>MALFORMED_FILE - The object is a malformed or corrupted file. An error occurred when Macie attempted to detect the file's type or extract data from the file.</p></li> <li><p>MALFORMED_OR_FILE_SIZE_EXCEEDS_LIMIT - The object is a Microsoft Office file that is malformed or exceeds the size quota for this type of file. If the file is malformed, an error occurred when Macie attempted to extract data from the file.</p></li> <li><p>NO_SUCH_BUCKET_AVAILABLE - The object was in a bucket that was deleted shortly before or when Macie attempted to analyze the object.</p></li> <li><p>OBJECT_VERSION_MISMATCH - The object was changed while Macie was analyzing it.</p></li> <li><p>OOXML_UNCOMPRESSED_RATIO_EXCEEDS_LIMIT - The object is an Office Open XML file whose compression ratio exceeds the compression quota for this type of file.</p></li> <li><p>OOXML_UNCOMPRESSED_SIZE_EXCEEDS_LIMIT - The object is an Office Open XML file that exceeds the size quota for this type of file.</p></li> <li><p>PERMISSION_DENIED - Macie isn't allowed to access the object. The object's permissions settings prevent Macie from analyzing the object.</p></li> <li><p>SOURCE_OBJECT_NO_LONGER_AVAILABLE - The object was deleted shortly before or when Macie attempted to analyze it.</p></li> <li><p>TIME_CUT_OFF_REACHED - Macie started analyzing the object but additional analysis would exceed the time quota for analyzing an object.</p></li> <li><p>UNABLE_TO_PARSE_FILE - The object is a file that contains structured data and an error occurred when Macie attempted to parse the data.</p></li> <li><p>UNSUPPORTED_FILE_TYPE_EXCEPTION - The object is a file that uses an unsupported file or storage format.</p></li></ul> <p>For information about quotas, supported storage classes, and supported file and storage formats, see <a href="https://docs.aws.amazon.com/macie/latest/user/macie-quotas.html">Quotas</a> and <a href="https://docs.aws.amazon.com/macie/latest/user/discovery-supported-storage.html">Supported storage classes and formats</a> in the <i>Amazon Macie User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ClassificationResultStatus) -> dict:
    out: dict = {}
    if "code" in value:
        out["code"] = value["code"]
    if "reason" in value:
        out["reason"] = value["reason"]
    return out


def deserialize_json(data: dict) -> ClassificationResultStatus:
    out: ClassificationResultStatus = {}  # type: ignore[typeddict-item]
    if data.get("code") is not None:
        out["code"] = data["code"]
    if data.get("reason") is not None:
        out["reason"] = data["reason"]
    return out
