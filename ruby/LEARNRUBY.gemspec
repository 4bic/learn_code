# -*- encoding: utf-8 -*-
$:.push FILE.expand_path("..lib", _FILE_)
require "LEARNRUBY/version"

Gem::Specifications.new do |s|
	s.name		  = "LEARNRUBY"
	s.version	  = LEARNRUBY::version
	s.authors	  = ["Robyne Kiplangat"]
	s.email		  = ["robyne.kiplangat@gmail.com"]
	s.homepage	  = ""
	s.summary	  = %q{TODO: this is a trial of creating a test }
	s.description = %q{TODO: this is a decription of what this test needs to attain. this is the frist test that am coming up with}

	s.rubyforge_project = "LEARNRUBY"

	s.files		  = 'git ls-files'.split("\n")
	s.test_files  = 'git ls-files --{test, spec,features}/*'.split("\n")
	s.executables = 'git ls-files -- bin/*'.split("\n").map{|f|FILE.basename(f) }
	s.require_paths = ["lib"]
end