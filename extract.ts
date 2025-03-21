import { globSync, readFileSync, writeFileSync } from 'node:fs';
import { basename, join } from 'node:path';

const topicAndKeywords = new Map([
	['elderly', ['elderly', 'older']], //
]);

for (const [topic, keywords] of topicAndKeywords) {
	const regex = new RegExp(`^.*?(${keywords.map((k) => `\\b${k}\\b`).join('|')}).*?$`, 'gim');
	const paths = globSync('./table-of-contents/*.txt');
	const matches = paths.flatMap((path) => {
		const text = readFileSync(path, { encoding: 'utf8' });
		return [...text.matchAll(regex)].map((match) =>
			`${match[0]} ('${basename(path, '.txt')})`
				.replace(/^paper *(\d+):?/i, 'Paper $1:')
				.replaceAll(/ {2,}/g, ' '),
		);
	});
	writeFileSync(join(import.meta.dirname, `/extracted/${topic}.txt`), matches.join('\n'));
}
