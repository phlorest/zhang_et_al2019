import pathlib

import phlorest


class Dataset(phlorest.Dataset):
    dir = pathlib.Path(__file__).parent
    id = "zhang_et_al2019"

    def cmd_makecldf(self, args):
        """
summary.trees: original/109SinoTibetanLanguages.MCC.tree
	cp $< $@

posterior.trees: original/Sino-Tibetan\ Posterior\ tree\ distribution.trees.gz
	# remove 1000 (10%), sample 1000
	nexus trees -c -d 1-1000 -n 1000 "$<" -o $@

data.nex:
	cp paper/41586_2019_1153_MOESM4_ESM/109SinoTibetanLanguages_Swadesh100.nex $@
        """
        self.init(args)
        with self.nexus_summary() as nex:
            self.add_tree_from_nexus(
                args,
                self.raw_dir / '109SinoTibetanLanguages.MCC.tree',
                nex,
                'summary',
                detranslate=True,
            )
        posterior = self.sample(
            self.remove_burnin(
                self.read_gzipped_text(
                    self.raw_dir / 'Sino-Tibetan Posterior tree distribution.trees.gz'),
                1000,
            ),
            detranslate=True,
            as_nexus=True)

        with self.nexus_posterior() as nex:
            for i, tree in enumerate(posterior.trees.trees, start=1):
                self.add_tree(args, tree, nex, 'posterior-{}'.format(i))

        self.add_data(args, self.raw_dir / '109SinoTibetanLanguages_Swadesh100-matched.nex')
