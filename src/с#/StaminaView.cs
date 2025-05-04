using UnityEngine;
using UnityEngine.UI;

public class StaminaView : MonoBehaviour
{
    [SerializeField] private Gradient _healthBarGradient;
    [SerializeField] private Image _staminaFilling;
    
    public void Display(float percentage)
    {
        _staminaFilling.fillAmount = percentage;
        _staminaFilling.color = _healthBarGradient.Evaluate(percentage);
    }
}
