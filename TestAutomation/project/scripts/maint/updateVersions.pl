#!/usr/bin/perl -w

$CONFIGURE_IN = '/home/aaron/theMonkeyCatfishCoalition/TestAutomation/project/configure.ac';
$ORCONFIG_H = '/home/aaron/theMonkeyCatfishCoalition/TestAutomation/project/src/win32/orconfig.h';
$TOR_NSI = '/home/aaron/theMonkeyCatfishCoalition/TestAutomation/project/contrib/win32build/tor-mingw.nsi.in';

$quiet = 1;

sub demand {
    my $fn = shift;
    die "Missing file $fn" unless (-f $fn);
}

demand($CONFIGURE_IN);
demand($ORCONFIG_H);
demand($TOR_NSI);

# extract version from configure.ac

open(F, $CONFIGURE_IN) or die "$!";
$version = undef;
while (<F>) {
    if (/AC_INIT\(\[tor\],\s*\[([^\]]*)\]\)/) {
	$version = $1;
	last;
    }
}
die "No version found" unless $version;
print "Tor version is $version\n" unless $quiet;
close F;

sub correctversion {
    my ($fn, $defchar) = @_;
    undef $/;
    open(F, $fn) or die "$!";
    my $s = <F>;
    close F;
    if ($s =~ /^$defchar(?:)define\s+VERSION\s+\"([^\"]+)\"/m) {
	$oldver = $1;
	if ($oldver ne $version) {
	    print "Version mismatch in $fn: It thinks that the version is $oldver.  I think it's $version.  Fixing.\n";
	    $line = $defchar . "define VERSION \"$version\"";
	    open(F, ">$fn.bak");
	    print F $s;
	    close F;
	    $s =~ s/^$defchar(?:)define\s+VERSION.*?$/$line/m;
	    open(F, ">$fn");
	    print F $s;
	    close F;
	} else {
	    print "$fn has the correct version. Good.\n" unless $quiet;
	}
    } else {
	print "Didn't find a version line in $fn -- uh oh.\n";
    }
}

correctversion($TOR_NSI, "!");
correctversion($ORCONFIG_H, "#");
