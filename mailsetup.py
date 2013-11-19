from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log
from os import path

class MailSetup(ClusterSetup):
	def __init__(self):
		None

	def run(self, nodes, master, user, user_shell, volumes):
		log.info("installing msmtp and mailx")
		# TODO: switch to package_install - in the current release
		# package_provider is broken, so we have to stick with
		# apt_install
		#master.package_install("msmtp bsd-mailx")
		master.apt_install("msmtp bsd-mailx")
		log.info("setting up rc files")
		master.ssh.switch_user(user)
		master.ssh.put(path.expanduser("~/.msmtprc"))
		master.ssh.execute("echo set sendmail=`which msmtp` >>~/.mailrc")
