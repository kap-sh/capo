"""Generated from Smithy shape ``com.amazonaws.glacier#GetJobOutputOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glacier.types.httpstatus
    import capo_glacier.types.stream
    import capo_glacier.types.string


class GetJobOutputOutput(TypedDict, closed=True):
    body: "capo_glacier.types.stream.Stream"
    """<p>The job data, either archive data or inventory data.</p>"""
    checksum: NotRequired["capo_glacier.types.string.string"]
    """<p>The checksum of the data in the response. This header is returned only when retrieving the output for an archive retrieval job. Furthermore, this header appears only under the following conditions:</p> <ul> <li> <p>You get the entire range of the archive.</p> </li> <li> <p>You request a range to return of the archive that starts and ends on a multiple of 1 MB. For example, if you have an 3.1 MB archive and you specify a range to return that starts at 1 MB and ends at 2 MB, then the x-amz-sha256-tree-hash is returned as a response header.</p> </li> <li> <p>You request a range of the archive to return that starts on a multiple of 1 MB and goes to the end of the archive. For example, if you have a 3.1 MB archive and you specify a range that starts at 2 MB and ends at 3.1 MB (the end of the archive), then the x-amz-sha256-tree-hash is returned as a response header.</p> </li> </ul>"""
    status: "capo_glacier.types.httpstatus.httpstatus"
    """<p>The HTTP response code for a job output request. The value depends on whether a range was specified in the request.</p>"""
    content_range: NotRequired["capo_glacier.types.string.string"]
    """<p>The range of bytes returned by Amazon Glacier. If only partial output is downloaded, the response provides the range of bytes Amazon Glacier returned. For example, bytes 0-1048575/8388608 returns the first 1 MB from 8 MB.</p>"""
    accept_ranges: NotRequired["capo_glacier.types.string.string"]
    """<p>Indicates the range units accepted. For more information, see <a href="http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html">RFC2616</a>. </p>"""
    content_type: NotRequired["capo_glacier.types.string.string"]
    """<p>The Content-Type depends on whether the job output is an archive or a vault inventory. For archive data, the Content-Type is application/octet-stream. For vault inventory, if you requested CSV format when you initiated the job, the Content-Type is text/csv. Otherwise, by default, vault inventory is returned as JSON, and the Content-Type is application/json.</p>"""
    archive_description: NotRequired["capo_glacier.types.string.string"]
    """<p>The description of an archive.</p>"""
