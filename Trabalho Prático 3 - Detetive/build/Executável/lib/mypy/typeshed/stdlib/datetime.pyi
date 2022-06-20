import sys
from time import struct_time
from typing import ClassVar, NamedTuple, NoReturn, SupportsAbs, Type, TypeVar, overload
from typing_extensions import final

_S = TypeVar("_S")
_D = TypeVar("_D", bound=date)

MINYEAR: int
MAXYEAR: int

class tzinfo:
    def tzname(self, __dt: datetime | None) -> str | None: ...
    def utcoffset(self, __dt: datetime | None) -> timedelta | None: ...
    def dst(self, __dt: datetime | None) -> timedelta | None: ...
    def fromutc(self, __dt: datetime) -> datetime: ...

# Alias required to avoid name conflicts with date(time).tzinfo.
_tzinfo = tzinfo

@final
class timezone(tzinfo):
    utc: ClassVar[timezone]
    min: ClassVar[timezone]
    max: ClassVar[timezone]
    def __init__(self, offset: timedelta, name: str = ...) -> None: ...
    def __hash__(self) -> int: ...

if sys.version_info >= (3, 9):
    class _IsoCalendarDate(NamedTuple):
        year: int
        week: int
        weekday: int

class date:
    min: ClassVar[date]
    max: ClassVar[date]
    resolution: ClassVar[timedelta]
    def __new__(cls: Type[_S], year: int, month: int, day: int) -> _S: ...
    @classmethod
    def fromtimestamp(cls: Type[_S], __timestamp: float) -> _S: ...
    @classmethod
    def today(cls: Type[_S]) -> _S: ...
    @classmethod
    def fromordinal(cls: Type[_S], __n: int) -> _S: ...
    if sys.version_info >= (3, 7):
        @classmethod
        def fromisoformat(cls: Type[_S], __date_string: str) -> _S: ...
    if sys.version_info >= (3, 8):
        @classmethod
        def fromisocalendar(cls: Type[_S], year: int, week: int, day: int) -> _S: ...
    @property
    def year(self) -> int: ...
    @property
    def month(self) -> int: ...
    @property
    def day(self) -> int: ...
    def ctime(self) -> str: ...
    def strftime(self, __format: str) -> str: ...
    def __format__(self, __fmt: str) -> str: ...
    def isoformat(self) -> str: ...
    def timetuple(self) -> struct_time: ...
    def toordinal(self) -> int: ...
    def replace(self, year: int = ..., month: int = ..., day: int = ...) -> date: ...
    def __le__(self, __other: date) -> bool: ...
    def __lt__(self, __other: date) -> bool: ...
    def __ge__(self, __other: date) -> bool: ...
    def __gt__(self, __other: date) -> bool: ...
    if sys.version_info >= (3, 8):
        def __add__(self: _S, __other: timedelta) -> _S: ...
        def __radd__(self: _S, __other: timedelta) -> _S: ...
        @overload
        def __sub__(self: _D, __other: timedelta) -> _D: ...
        @overload
        def __sub__(self, __other: datetime) -> NoReturn: ...
        @overload
        def __sub__(self: _D, __other: _D) -> timedelta: ...
    else:
        # Prior to Python 3.8, arithmetic operations always returned `date`, even in subclasses
        def __add__(self, __other: timedelta) -> date: ...
        def __radd__(self, __other: timedelta) -> date: ...
        @overload
        def __sub__(self, __other: timedelta) -> date: ...
        @overload
        def __sub__(self, __other: datetime) -> NoReturn: ...
        @overload
        def __sub__(self, __other: date) -> timedelta: ...
    def __hash__(self) -> int: ...
    def weekday(self) -> int: ...
    def isoweekday(self) -> int: ...
    if sys.version_info >= (3, 9):
        def isocalendar(self) -> _IsoCalendarDate: ...
    else:
        def isocalendar(self) -> tuple[int, int, int]: ...

class time:
    min: ClassVar[time]
    max: ClassVar[time]
    resolution: ClassVar[timedelta]
    def __new__(
        cls: Type[_S],
        hour: int = ...,
        minute: int = ...,
        second: int = ...,
        microsecond: int = ...,
        tzinfo: _tzinfo | None = ...,
        *,
        fold: int = ...,
    ) -> _S: ...
    @property
    def hour(self) -> int: ...
    @property
    def minute(self) -> int: ...
    @property
    def second(self) -> int: ...
    @property
    def microsecond(self) -> int: ...
    @property
    def tzinfo(self) -> _tzinfo | None: ...
    @property
    def fold(self) -> int: ...
    def __le__(self, __other: time) -> bool: ...
    def __lt__(self, __other: time) -> bool: ...
    def __ge__(self, __other: time) -> bool: ...
    def __gt__(self, __other: time) -> bool: ...
    def __hash__(self) -> int: ...
    def isoformat(self, timespec: str = ...) -> str: ...
    if sys.version_info >= (3, 7):
        @classmethod
        def fromisoformat(cls: Type[_S], __time_string: str) -> _S: ...
    def strftime(self, __format: str) -> str: ...
    def __format__(self, __fmt: str) -> str: ...
    def utcoffset(self) -> timedelta | None: ...
    def tzname(self) -> str | None: ...
    def dst(self) -> timedelta | None: ...
    def replace(
        self,
        hour: int = ...,
        minute: int = ...,
        second: int = ...,
        microsecond: int = ...,
        tzinfo: _tzinfo | None = ...,
        *,
        fold: int = ...,
    ) -> time: ...

_date = date
_time = time

class timedelta(SupportsAbs[timedelta]):
    min: ClassVar[timedelta]
    max: ClassVar[timedelta]
    resolution: ClassVar[timedelta]
    def __new__(
        cls: Type[_S],
        days: float = ...,
        seconds: float = ...,
        microseconds: float = ...,
        milliseconds: float = ...,
        minutes: float = ...,
        hours: float = ...,
        weeks: float = ...,
    ) -> _S: ...
    @property
    def days(self) -> int: ...
    @property
    def seconds(self) -> int: ...
    @property
    def microseconds(self) -> int: ...
    def total_seconds(self) -> float: ...
    def __add__(self, __other: timedelta) -> timedelta: ...
    def __radd__(self, __other: timedelta) -> timedelta: ...
    def __sub__(self, __other: timedelta) -> timedelta: ...
    def __rsub__(self, __other: timedelta) -> timedelta: ...
    def __neg__(self) -> timedelta: ...
    def __pos__(self) -> timedelta: ...
    def __abs__(self) -> timedelta: ...
    def __mul__(self, __other: float) -> timedelta: ...
    def __rmul__(self, __other: float) -> timedelta: ...
    @overload
    def __floordiv__(self, __other: timedelta) -> int: ...
    @overload
    def __floordiv__(self, __other: int) -> timedelta: ...
    @overload
    def __truediv__(self, __other: timedelta) -> float: ...
    @overload
    def __truediv__(self, __other: float) -> timedelta: ...
    def __mod__(self, __other: timedelta) -> timedelta: ...
    def __divmod__(self, __other: timedelta) -> tuple[int, timedelta]: ...
    def __le__(self, __other: timedelta) -> bool: ...
    def __lt__(self, __other: timedelta) -> bool: ...
    def __ge__(self, __other: timedelta) -> bool: ...
    def __gt__(self, __other: timedelta) -> bool: ...
    def __bool__(self) -> bool: ...
    def __hash__(self) -> int: ...

class datetime(date):
    min: ClassVar[datetime]
    max: ClassVar[datetime]
    resolution: ClassVar[timedelta]
    def __new__(
        cls: Type[_S],
        year: int,
        month: int,
        day: int,
        hour: int = ...,
        minute: int = ...,
        second: int = ...,
        microsecond: int = ...,
        tzinfo: _tzinfo | None = ...,
        *,
        fold: int = ...,
    ) -> _S: ...
    @property
    def hour(self) -> int: ...
    @property
    def minute(self) -> int: ...
    @property
    def second(self) -> int: ...
    @property
    def microsecond(self) -> int: ...
    @property
    def tzinfo(self) -> _tzinfo | None: ...
    @property
    def fold(self) -> int: ...
    # The first parameter in `fromtimestamp` is actually positional-or-keyword,
    # but it is named "timestamp" in the C implementation and "t" in the Python implementation,
    # so it is only truly *safe* to pass it as a positional argument.
    @classmethod
    def fromtimestamp(cls: Type[_S], __timestamp: float, tz: _tzinfo | None = ...) -> _S: ...
    @classmethod
    def utcfromtimestamp(cls: Type[_S], __t: float) -> _S: ...
    if sys.version_info >= (3, 8):
        @classmethod
        def now(cls: Type[_S], tz: _tzinfo | None = ...) -> _S: ...
    else:
        @overload
        @classmethod
        def now(cls: Type[_S], tz: None = ...) -> _S: ...
        @overload
        @classmethod
        def now(cls, tz: _tzinfo) -> datetime: ...
    @classmethod
    def utcnow(cls: Type[_S]) -> _S: ...
    @classmethod
    def combine(cls, date: _date, time: _time, tzinfo: _tzinfo | None = ...) -> datetime: ...
    if sys.version_info >= (3, 7):
        @classmethod
        def fromisoformat(cls: Type[_S], __date_string: str) -> _S: ...
    def timestamp(self) -> float: ...
    def utctimetuple(self) -> struct_time: ...
    def date(self) -> _date: ...
    def time(self) -> _time: ...
    def timetz(self) -> _time: ...
    def replace(
        self,
        year: int = ...,
        month: int = ...,
        day: int = ...,
        hour: int = ...,
        minute: int = ...,
        second: int = ...,
        microsecond: int = ...,
        tzinfo: _tzinfo | None = ...,
        *,
        fold: int = ...,
    ) -> datetime: ...
    if sys.version_info >= (3, 8):
        def astimezone(self: _S, tz: _tzinfo | None = ...) -> _S: ...
    else:
        def astimezone(self, tz: _tzinfo | None = ...) -> datetime: ...
    def ctime(self) -> str: ...
    def isoformat(self, sep: str = ..., timespec: str = ...) -> str: ...
    @classmethod
    def strptime(cls, __date_string: str, __format: str) -> datetime: ...
    def utcoffset(self) -> timedelta | None: ...
    def tzname(self) -> str | None: ...
    def dst(self) -> timedelta | None: ...
    def __le__(self, __other: datetime) -> bool: ...  # type: ignore[override]
    def __lt__(self, __other: datetime) -> bool: ...  # type: ignore[override]
    def __ge__(self, __other: datetime) -> bool: ...  # type: ignore[override]
    def __gt__(self, __other: datetime) -> bool: ...  # type: ignore[override]
    if sys.version_info >= (3, 8):
        @overload  # type: ignore[override]
        def __sub__(self: _D, __other: timedelta) -> _D: ...
        @overload
        def __sub__(self: _D, __other: _D) -> timedelta: ...
    else:
        # Prior to Python 3.8, arithmetic operations always returned `datetime`, even in subclasses
        def __add__(self, __other: timedelta) -> datetime: ...
        def __radd__(self, __other: timedelta) -> datetime: ...
        @overload  # type: ignore[override]
        def __sub__(self, __other: datetime) -> timedelta: ...
        @overload
        def __sub__(self, __other: timedelta) -> datetime: ...
    if sys.version_info >= (3, 9):
        def isocalendar(self) -> _IsoCalendarDate: ...
    else:
        def isocalendar(self) -> tuple[int, int, int]: ...
