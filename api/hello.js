import express from 'express';
const router = express.Router();

router.get('/', async (req, res) => {
	try {
		res.json({
			'Hello': 'World',
		});
	} catch (error) {
		console.error(error);
		return res.status(500).send('Server error');
	}
});

export default router;
