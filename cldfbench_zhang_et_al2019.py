import pathlib

import phlorest


class Dataset(phlorest.Dataset):
    dir = pathlib.Path(__file__).parent
    id = "zhang_et_al2019"
    
    def cmd_makecldf(self, args):
        self.init(args)

        args.writer.add_summary(
            self.raw_dir.read_tree(
                '109SinoTibetanLanguages.MCC.tree', detranslate=True),
            self.metadata,
            args.log)

        posterior = self.raw_dir.read_trees(
            'Sino-Tibetan Posterior tree distribution.trees.gz',
            burnin=1000, sample=1000, detranslate=True)
        args.writer.add_posterior(posterior, self.metadata, args.log)

        args.writer.add_data(
            self.raw_dir.read_nexus('109SinoTibetanLanguages_Swadesh100-matched.nex'),
            self.characters, 
            args.log)
    