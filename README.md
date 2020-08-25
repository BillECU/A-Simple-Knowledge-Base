# A-Simple-Knowledge-Base

<B>Algorithm</B>: 
Definite clause theorem

<B>Commands</B>:

load someKB.txt: This loads into memory the KB stored in the file someKB.txt

tell atom_1 atom_2 ... atom_n: This adds the atoms atom_1 to atom_n to the current KB

infer_all: Prints all the atoms that can currently be inferred by the rules in the KB. Note that no atoms can be inferred until at least one tell command is called.

stop: Stops the program



<B>Example</B>:

I create a KB about basic junior high school chemistry about hazardous chemicals.

I introduce some common ones via chemical formula.

They are based on oxygen, hydrogen, carbon, sulfur, chlorine, natrium, and nitrogen.

Most of them have to mix with oxygen because strongly acidic is more famous than strongly alkaline.

<B>Example Code</B>:

kb>load kb_example.txt

water <-- oxygen & hydrogen 
oxocarbon <-- carbon & oxygen
carbonic_acid <-- oxocarbon & water
sulfurous_oxychloride <-- sulfur & oxygen
sulfuric_acid <-- sulfurous_oxychloride & water
hydrogen_peroxide <-- hydrogen & oxygen
hydrochloric_acid <-- sulfurous_oxychloride & chlorine & water
sodium <-- natrium & chlorine
sodium_hydroxide <-- sodium & water
nitric_oxide <-- nitrogen & oxygen
nitric_acid <-- nitric_oxide & water
aqua_regia <-- carbonic_acid & nitric_acid

12 new rule(s) added

kb>infer_all

Newly inferred atoms:
	<none>
Atoms already known to be true:
	<none>

kb>tell oxygen carbon

"oxygen" added to KB
"carbon" added to KB

kb>infer_all

Newly inferred atoms:
	 oxocarbon
Atoms already known to be true:
	 oxygen, carbon

kb>tell

Error: tell needs at least one atom

kb>tell hydrogen

"hydrogen" added to KB

kb>infer_all

Newly inferred atoms:
	 water hydrogen_peroxide carbonic_acid
Atoms already known to be true:
	 oxocarbon, oxygen, carbon, hydrogen

kb>tell natrium chlorine

"natrium" added to KB
"chlorine" added to KB

kb>infer_all
Newly inferred atoms:
	 sodium sodium_hydroxide
Atoms already known to be true:
	 water, hydrogen_peroxide, carbonic_acid, water, hydrogen_peroxide, water, oxocarbon, oxygen, carbon, hydrogen, natrium, chlorine

kb>infer_all
Newly inferred atoms:
	<none>
Atoms already known to be true:
	 sodium, sodium_hydroxide, sodium, water, hydrogen_peroxide, carbonic_acid, water, hydrogen_peroxide, water, oxocarbon, oxygen, carbon, hydrogen, natrium, chlorine

kb>stop

